from django.conf.urls import url
from django.http import JsonResponse, HttpResponseBadRequest
import pickle

def getPickleData(request, object_name):
    '''
    Retrieve object from URL parameter and load the pickled object
    '''
    try:
        # Retrieve the pickled data from the GET parameter
        pickled = request.GET.get(object_name)
        if not pickled:
            return HttpResponseBadRequest("No data provided for the specified object.")

        # Decode and unpickle the data
        pickled_bytes = bytes(pickled, 'utf-8')  # Convert string to bytes
        defoliated = pickle.loads(pickled_bytes)

        # Return the unpickled object as a JSON response
        return JsonResponse({'data': defoliated})
    except pickle.UnpicklingError:
        return HttpResponseBadRequest("Invalid pickled data.")
    except Exception as e:
        return HttpResponseBadRequest(f"An error occurred: {str(e)}")


from django.urls import path
   from .views import getPickleData

   urlpatterns = [
       path('get-pickle-data/<str:object_name>/', getPickleData, name='get_pickle_data'),
   ]
