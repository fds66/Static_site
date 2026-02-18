from enum import Enum
from textnode import TextNode, TextType
from htmlnode import HTMLNode,LeafNode,ParentNode
from textnode_to_htmlnode import text_node_to_html_node
from split_nodes_delimiter import split_nodes_delimiter


'''
for reference
class TextType(Enum):
    TEXT = "text(plain)"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "'Code text'"
    LINK = "[anchor text](url)"
    IMAGES = "![alt text](url)"
    '''


def main():
    print("running main")
    

    node = TextNode("This is text with an _italic_ word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.ITALIC)
    print(new_nodes)   


    '''
    #new_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    #new_node = TextNode("This is some test text", TextType.BOLD)
    new_node = node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    result = text_node_to_html_node(new_node)
    print(result)
    

    props = {"href": "https://www.google.com","target": "_blank",}
    #new_html_node = LeafNode("a","this is the text",props)
    new_html_node = LeafNode("p","this is the text")
    result = new_html_node.to_html()
    print(result)

    new_html_node = LeafNode("p", "This is a paragraph of text.")
    result = new_html_node.to_html()
    expected = "<p>This is a paragraph of text.</p>"
    print(f"actual,{result}, expected,{expected}")
    
    node = ParentNode("p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ParentNode("a",[LeafNode("b","Nested parent")])
    ],
    )
    node2 = ParentNode("a",[LeafNode("b","Nested parent")])
    result = node.to_html()
    print(result)
    result = node2.to_html()
    print(result)
    
    node = ParentNode("p",[LeafNode("b","This is a leaf")])
    result = node.__repr__()
    print(result)
    
    print("testing repr")
    node = ParentNode("p",[LeafNode("b","This is a leaf")])
    result = node.__repr__()
    expected = "ParentNode(p, [LeafNode(b, This is a leaf, None)], None)"
    print(result,expected)
    
    print("testing props")
    props = {"href": "https://www.google.com","target": "_blank",}
    node = ParentNode("p",LeafNode("b","Text"),props)
    result = node.props_to_html()
    expected = ' href="https://www.google.com" target="_blank"'    
    print(result, expected)
      
    
        
    print("testing blank props")   
    result = ParentNode("p",LeafNode("b","Text")).props_to_html()
    expected = ""   
    print(result, expected)
    '''
    


main()