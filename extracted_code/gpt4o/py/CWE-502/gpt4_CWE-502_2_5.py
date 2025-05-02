from django.conf.urls import url
from django.http import JsonResponse, HttpResponseBadRequest
import pickle
import base64

# View function to handle pickled data
def getPickleData(request, pickled_object):
    """
    Convert a pickled string back into an object and return it as JSON.
    """
    try:
        # Decode the base64-encoded pickled string
        decoded_data = base64.b64decode(pickled_object)
        
        # Unpickle the data
        unpickled_object = pickle.loads(decoded_data)
        
        # Return the unpickled object as a JSON response
        return JsonResponse({'data': unpickled_object})
    except (pickle.UnpicklingError, ValueError, TypeError) as e:
        # Handle errors during unpickling or decoding
        return HttpResponseBadRequest(f"Invalid pickled data: {str(e)}")

# URL patterns
urlpatterns = [
    url(r'^get-pickle-data/(?P<pickled_object>.+)/$', getPickleData, name='get_pickle_data'),
]
