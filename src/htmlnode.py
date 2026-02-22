

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
        #print(f"props is {self.props} for this {self.__repr__()}\n")
        if self.props:
            props_html = ""
            for prop in self.props:
                #print(f"prop is {prop}")
                #print(f" self.props[prop] is {self.props[prop]}/n")
                props_html += f' {prop}="{self.props[prop]}"' 
            #f' href="{self.props[href]}" target="{self.props[target]}"'
            return props_html
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
    
############################################################################################

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)
        #self.props = props

    def to_html(self):
        if not self:
            raise ValueError ("LeafNode has not value")
        if self.tag == None:
            return self.value
        #print(f"processing {self.__repr__()}")
        #props_string = self.props_to_html()
        
        return  f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
            
        '''
        Required format
        LeafNode("p", "This is a paragraph of text.").to_html()
        "<p>This is a paragraph of text.</p>"
        LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        '<a href="https://www.google.com">Click me!</a>'
        '''

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

 ############################################################################################      
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if not self.children:
            raise ValueError ("ParentNode has no children")
        if self.tag == None:
            raise ValueError ("ParentNode does not have a tag")
        final_string = f"<{self.tag}{self.props_to_html()}>"
        #strings=[]
        for child in self.children:
            final_string += child.to_html()
        final_string += f"</{self.tag}>"
        return final_string
    
    '''
    Example given
    node = ParentNode( "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )

    node.to_html()
    gives:
    <p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>
    if pretty printed it would look like this
    <p>
     <b>Bold text</b>
     Normal text
     <i>italic text</i>
     Normal text
    </p>

'''
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
    