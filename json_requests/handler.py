from . import notification_handler
from django.http import JsonResponse
from . import document_upload
action_map = {
    'notification': notification_handler,
    'document upload': document_upload
}


def handle_request(request: dict):
    try:
        action = request['action']['data']
        operation = request['actai  on']['operation']
    except KeyError:
        return JsonResponse({'status': 'error', 'cause':'invalid-request'})

    if action not in action_map:
        return JsonResponse({"status": "error", "cause": "unknown operation"})
    return action_map[action].handle(operation)
