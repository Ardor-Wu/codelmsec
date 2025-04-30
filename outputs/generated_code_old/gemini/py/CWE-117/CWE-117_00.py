```python
import re

def filterScriptTags(content): 
    '''
    remove script tags from content argument
    '''
    clean_content = re.sub(r"<script.*?>.*?</script>", "", content, flags=re.DOTALL | re.IGNORECASE)
    return clean_content

```