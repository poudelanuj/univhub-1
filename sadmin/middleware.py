

class CorsMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response=self.get_response(request)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers']='Origin, X-Requested-With, Content-Type, Accept, X-CSRF-TOKEN'
        response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT'
        return response