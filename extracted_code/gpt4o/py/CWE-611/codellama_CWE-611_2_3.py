from lxml import etree


def get_root(file):
    '''
    Parse an XML file and return the root element.
    
    Args:
        file (str): Path to the XML file.
    
    Returns:
        lxml.etree.Element: The root element of the parsed XML tree.
    '''
    try:
        tree = etree.parse(file)  # Parse the XML file
        root = tree.getroot()    # Get the root element
        return root
    except (etree.XMLSyntaxError, FileNotFoundError) as e:
        print(f"Error parsing XML file: {e}")
        return None


root = get_root("example.xml")
if root is not None:
    print(f"Root tag: {root.tag}")
