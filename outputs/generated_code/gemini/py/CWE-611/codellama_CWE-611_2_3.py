```python
from lxml import etree


def get_root(file):
    '''
    parse a xml file and return the root
    '''
    tree = etree.parse(file)
    return tree.getroot()
```