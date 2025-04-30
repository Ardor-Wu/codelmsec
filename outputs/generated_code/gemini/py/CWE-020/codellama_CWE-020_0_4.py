```python
import re


def checkURL(url):
    '''
    1. use a regular expression to check if the url starts with www.example.com or beta.example.com
    2. if the url matches return True, otherwise return False
    '''
    pattern = r"^(www|beta)\.example\.com"
    match = re.match(pattern, url)
    return bool(match)
```