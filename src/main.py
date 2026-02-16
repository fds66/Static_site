from enum import Enum
from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    '''
    new_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(new_node)
    print(new_node.__repr__)
    print(TextType.LINK.value)
    '''
    props = {"href": "https://www.google.com","target": "_blank",}
    new_html_node = HTMLNode("p","this is the text",None,props)
    result = new_html_node.props_to_html()
    print(result)

    node = HTMLNode("p","Node 1")
    
    result1 = node.__repr__()
    
    print(result1)
    



main()