```python
import re


def is_valid_url(url):
    '''
    1. check if the url contains "example.com"
    2. if it does, check if it starts with "www" or ""
    3. if it does, check if it contains only alphanumeric characters, ".", and "-"
    4. if it does, return True
    5. otherwise, return False
    '''
    if "example.com" not in url:
        return False

    if not (url.startswith("www.") or url.startswith("")):
        return False

    pattern = r"^[\w.-]+$"  # Corrected regex
    if url.startswith("www."):
        url_without_www = url[4:]  # Remove "www."
        return bool(re.match(pattern, url_without_www))
    else:
        return bool(re.match(pattern, url))


```