import re


def checkURL(url):
    '''
    1. Use a regular expression to check if the URL starts with www.example.com or beta.example.com
    2. If the URL matches, return True. Otherwise, return False.
    '''
    # Define the regular expression pattern
    pattern = r'^(www\.example\.com|beta\.example\.com)'

    # Use re.match to check if the URL matches the pattern
    if re.match(pattern, url):
        return True
    else:
        return False


# Example usage:
print(checkURL("www.example.com/page"))  # True
print(checkURL("beta.example.com/page"))  # True
print(checkURL("test.example.com/page"))  # False
print(checkURL("example.com/page"))  # False
