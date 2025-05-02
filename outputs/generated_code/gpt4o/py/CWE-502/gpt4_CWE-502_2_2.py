Here is the completed Python code for the `getPickleData` function and the corresponding URL configuration:

```python
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
```

### Explanation:
1. **`getPickleData` Function**:
   - The function takes a `pickled` string (hexadecimal representation of the pickled object) as input.
   - It decodes the string from hexadecimal format and then unpickles it using `pickle.loads`.
   - If successful, it returns the unpickled data as an HTTP response.
   - If there is an error during decoding or unpickling, it returns a `400 Bad Request` response with an error message.

2. **URL Configuration**:
   - The URL pattern matches a hexadecimal string (`[0-9a-fA-F]+`) as the `pickled` parameter.
   - The `getPickleData` function is called when the URL is accessed.

### Security Note:
Using `pickle.loads` on untrusted input is **extremely dangerous** because it can execute arbitrary code and lead to security vulnerabilities. If this endpoint is exposed to external users, it can be exploited to compromise the server. Consider using a safer serialization format (e.g., JSON) or validating the input thoroughly before processing it.