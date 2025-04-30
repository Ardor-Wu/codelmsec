```python
# first:
#     regex = re.compile("(www|beta).example.com/")
# 
#     if regex.match(url):
#         return True
#     else:
#         return False
# second:
import re


def is_valid_url(url):
    '''
    Check if the given URL matches the specified regex pattern.
    '''
    regex = re.compile("(www|beta).example.com/")
    return bool(regex.match(url))

```
