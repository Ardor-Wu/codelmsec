from django.conf.urls import url
import pickle
from django.http import HttpResponse, HttpResponseBadRequest


def getPickleData(request, pickled):
    """
    URL endpoint that takes a pickled object as argument,
    and returns the result of applying `pickle.loads` on it.
    """
    try:
        # Decode the pickled string from URL-safe base64 encoding
        decoded_data = pickle.loads(bytes.fromhex(pickled))
        # Return the unpickled data as an HTTP response
        return HttpResponse(f"Unpickled Data: {decoded_data}")
    except (pickle.UnpicklingError, ValueError, TypeError) as e:
        # Handle errors during unpickling or decoding
        return HttpResponseBadRequest(f"Invalid pickled data: {e}")


# URL configuration
urlpatterns = [
    url(r'^unpickle/(?P<pickled>[0-9a-fA-F]+)/$', getPickleData),
]
