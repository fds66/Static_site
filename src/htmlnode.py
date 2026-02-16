

#tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
#value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
#children - A list of HTMLNode objects representing the children of this node
#props - A dictionary of key-value pairs representing the attributes of the HTML tag.
#  For example, a link (<a> tag) might have {"href": "https://www.google.com"}

class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError ("Not implemented yet")
    
    def props_to_html(self):
        if self.props:
            href = "href"
            target = "target"
            return f' href="{self.props[href]}" target="{self.props[target]}"'
        else:
            return ""
    # href="https://www.google.com" target="_blank" 
    # from this props:
    # {
    # "href": "https://www.google.com",
    # "target": "_blank",
    # } 


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"