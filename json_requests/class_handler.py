
def handle(request, operation):
    if operation in operations:
        return operations['operation'](request)
    else:
        return JsonResponse({'status': 'Error', 'reason': "Invalid operation specified :" + operation})


from django.http import JsonResponse

def register_class(request):
    return JsonResponse({'return':False,'reason':"Not implemented yet"})

def list_class(request):

    return JsonResponse([{"name": "Toefl", "date": "7th june-6th july", "tutor": "zenish shrestha", "location": "Chabahil",
      "stat": "Register"},
     {"name": "Ielts", "date": "1th june-9th august", "tutor": "shova thapa", "location": "pulchowk",
      "stat": "Registered"}],safe=False);

operations={
    'register':register_class,
    'list':list_class
}