from django.http import JsonResponse
from django.urls import re_path
import json

# Define the view function
def get_serialized_data(request, object):
    """
    Deserialize the given JSON object and return it.
    """
    try:
        # Replace '+' with space and deserialize the JSON object
        deserialized = json.loads(object.replace('+', ' '))
        return JsonResponse({'success': True, 'data': deserialized})
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'error': 'Invalid JSON object'}, status=400)

# Define the URL pattern
urlpatterns = [
    re_path(r'^(?P<object>.*)$', get_serialized_data),
]
