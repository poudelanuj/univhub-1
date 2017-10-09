'''
Handles all the incoming requests and redirects them into corresponding function of handlers.

'''
import pkgutil
from django.http import JsonResponse
import sys, importlib
import traceback


def error_response(error: str, code=404):
    if code == 500:
        traceback.print_exc()
    response = JsonResponse(
        {"status": "error", "cause": error})
    response.status_code = code
    return response


def __initialize__():
    modules = [name for _, name, _ in pkgutil.iter_modules(['json_requests']) if
               name != 'handler' and name.endswith('_handler')]
    action_map = {}
    for x in modules:
        name = x[:-8]
        action_map[name] = importlib.import_module('.' + x, 'json_requests')

    operation_map = {}
    for x in action_map:

        size = len(x) + 1
        op = [y for y in dir(action_map[x]) if y.endswith('_' + x)]
        names = [y[:-size] for y in op]
        # print(op)
        operation_map[x] = {}

        for operation, name in zip(op, names):
            operation_map[x][name] = getattr(action_map[x], operation)
            # print(operation_map)
    return operation_map


def handle_request(request):
    try:
        action = request['action']['data']
        operation = request['action']['operation']
    except KeyError:
        error_response('JSON action field is not valid ')
    del request['action']
    return handle_request_direct(action, operation, request)


def handle_request_direct(action, operation, request):
    if action not in action_map:
        error_response("Unknown action data : " + action)

    if operation not in action_map[action]:
        error_response(action + " doesn't have operation " + operation)
    try:
        response = action_map[action][operation](request)
        if response is None:
            return error_response("Internal Server error while serving request '" + operation + "' on '" + action + "' data", 500)
    except:
        return error_response("Internal Server error while serving request '" + operation + "' on '" + action + "' data", 500)


action_map = __initialize__()
