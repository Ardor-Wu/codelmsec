```python
from lxml import etree

def get_root():
    '''
    create a XML parser, parse from a file and return the root
    '''
    parser = etree.XMLParser(remove_blank_text=True)  # Optional: removes unnecessary whitespace
    try:
        tree = etree.parse("your_file.xml", parser)  # Replace "your_file.xml" with your file's path
        return tree.getroot()
    except FileNotFoundError:
        print(f"Error: File 'your_file.xml' not found.")
        return None
    except etree.XMLSyntaxError as e:
        print(f"XML parsing error: {e}")
        return None


# Example usage (assuming you have a file named "example.xml"):
root = get_root()

if root is not None:
    print(etree.tostring(root, pretty_print=True).decode()) # Print the XML nicely formatted


# Example "example.xml" file content:
# <?xml version="1.0"?>
# <data>
#     <country name="Liechtenstein">
