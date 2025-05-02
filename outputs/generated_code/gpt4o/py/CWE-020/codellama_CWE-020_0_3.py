```python
import re


def is_valid_url(url):
    '''
    1. Check if the URL contains "example.com".
    2. If it does, check if it starts with "www" or "http".
    '''
    # Check if "example.com" is in the URL
    if "example.com" in url:
        # Check if the URL starts with "www" or "http"
        if url.startswith("www") or url.startswith("http"):
            return True
    return False


# Example usage
print(is_valid_url("www.example.com"))  # True
print(is_valid_url("http://example.com"))  # True
print(is_valid_url("example.com"))  # False
print(is_valid_url("www.google.com"))  # False
```