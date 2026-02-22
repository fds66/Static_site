from enum import Enum
from textnode import TextType,TextNode
from htmlnode import HTMLNode,LeafNode,ParentNode

# reminder of enum types
'''class TextType(Enum):
    TEXT = "text(plain)"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "'Code text'"
    LINK = "[anchor text](url)"
    IMAGES = "![alt text](url)"'''



   # Function to convert text node to html node


def text_node_to_html_node(text_node):
    #print("entering text node to html node function")
    
    
    if  text_node.text_type not in TextType:
        raise Exception ("text_type is not part of the TextType enum")
    
    '''class TextNode():
    def __init__(self,text,text_type: TextType,url=None):
        class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)
        class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
    '''
    
    match text_node.text_type:

        case TextType.TEXT:
            return LeafNode(None,text_node.text)

        case TextType.BOLD:
            return LeafNode("b",text_node.text)

        case TextType.ITALIC:
            return LeafNode("i",text_node.text)
            
        case TextType.CODE:
            return LeafNode("code",text_node.text)

        case TextType.LINK:
            
            return LeafNode("a",text_node.text,{"href": text_node.url})

        case TextType.IMAGE:
            
            return LeafNode("img","",{"src": text_node.url,"alt": text_node.text})
        
           
        case _:
            result = f"no known texttype selected"
            return result
    



    
    