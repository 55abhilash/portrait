from tmp_pre.views import fn

class tmp_middleware(object):
    def process_response(self, request, response):
        response.content = str(fn(request)) + response.content 
        return response
