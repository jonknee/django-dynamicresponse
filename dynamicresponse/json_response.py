from django.http import HttpResponse
from dynamicresponse.emitters import JSONEmitter

class JsonResponse(HttpResponse):
    """
    Provides a JSON response to a client, performing automatic serialization.
    """
    
    def __init__(self, object, fields=(), custom_fields=False, status=200):
        
        # Perform JSON serialization
        emitter = JSONEmitter(object, {}, None, fields=fields, custom_fields=custom_fields)
        content = emitter.render()
        
        # Return response with correct payload/type
        super(JsonResponse, self).__init__(content, status=status, mimetype='application/json')
