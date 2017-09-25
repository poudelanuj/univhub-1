from . import notification_handler
from django.http import JsonResponse
from . import document_upload
from . import class_handler

action_map = {
    'notification': notification_handler,
    'document upload': document_upload,
    'class': class_handler
}


def handle_request(request: dict):
    try:
        action = request['action']['data']
        operation = request['action']['operation']
    except KeyError:
        return JsonResponse({'status': 'error', 'cause': 'invalid-request'})

    if action not in action_map:
        return JsonResponse({"status": "error", "cause": "unknown operation"})
    del request['action']
    return action_map[action].handle(request, operation)
