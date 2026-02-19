import re
from enum import Enum
import pprint

from textnode import TextType,TextNode
from htmlnode import HTMLNode,LeafNode,ParentNode
from extract_markdown import extract_markdown_images,extract_markdown_links
from textnode_to_htmlnode import text_node_to_html_node
from split_nodes import split_nodes_delimiter,split_nodes_image,split_nodes_link




'''
examples:
INPUT
This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)

OUTPUT
[
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
]

# reminder of enum types
class TextType(Enum):
    TEXT = "text(plain)"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "'Code text'"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"
    
    
    class TextNode():
    def __init__(self,text,text_type: TextType,url=None):
 


'''
def text_to_textnodes(text):
    
    original_textnode = TextNode(text,TextType.TEXT)
    bold_nodes = split_nodes_delimiter([original_textnode],"**",TextType.BOLD)
    #print("after bold")
    #pprint.pprint (bold_nodes)
    italic_nodes = split_nodes_delimiter(bold_nodes,"_",TextType.ITALIC)
    #print("after italic")
    #pprint.pprint (italic_nodes)
    code_nodes = split_nodes_delimiter(italic_nodes,"`",TextType.CODE)
    #print("after code")
    #pprint.pprint (code_nodes)
    image_nodes = split_nodes_image(code_nodes)
    #print("after image ")
    #pprint.pprint (image_nodes)
    link_nodes = split_nodes_link(image_nodes)
    #print("after link ")
    #pprint.pprint (link_nodes)
    final_nodes = link_nodes
    
    return final_nodes