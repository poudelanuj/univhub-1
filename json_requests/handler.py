'''
Handles all the incoming requests and redirects them into corresponding function of handlers.

'''
import pkgutil
from django.http import JsonResponse
import sys, importlib


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
        return JsonResponse({'status': 'error', 'cause': 'action field is invalid'})
    del request['action']
    return handle_request_direct(action,operation,request)

action_map = __initialize__()


def handle_request_direct(action, operation, request):
    if action not in action_map:
        return JsonResponse({"status": "error", "cause": "Unknown action data : " + action})

    if operation not in action_map[action]:
        return JsonResponse({"status": "error", "cause": "" + action + " doesn't have operation " + operation})
    try:
        response= action_map[action][operation](request)
        if response is None:
            return JsonResponse({"status": "error", "cause": action+"'s "+operation+" handler returned nothing"})
        return response
    except Exception as e:
        return JsonResponse({"status": "error", "cause": "Internal Server Error while serving request " + operation})
