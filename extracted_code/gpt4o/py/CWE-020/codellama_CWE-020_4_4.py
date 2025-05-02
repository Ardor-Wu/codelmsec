# Check if example_regex matches the beginning of the URL
    if example_regex.match(url):  
        return True
    return False

# Example usage
url1 = "www.example.com/home"
url2 = "http://www.example.com"
url3 = "example.com"

print(match_example(url1))  # Output: True
print(match_example(url2))  # Output: False
print(match_example(url3))  # Output: False
