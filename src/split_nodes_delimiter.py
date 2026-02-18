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
    IMAGES = "![alt text](url)"
    
    
    class TextNode():
    def __init__(self,text,text_type: TextType,url=None):
 
 '''





def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #print("running split nodes delimiter")

            

    list_of_new_nodes =[]
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            list_of_new_nodes.append(old_node)
        else:
            string_list = old_node.text.split(delimiter)
            #print(string_list)
            if len(string_list)%2 == 0:
                raise ValueError ("Invalid Markdown syntax, closing delimiter not found")

            for i in range(len(string_list)):
                #if an empty string then skip it
                if string_list[i] == "":
                    continue
                #if even 0,2,4,...then TextType.TEXT
                if i%2 == 0:
                    #new_node = TextNode(f'"{string_list[i]}"',TextType.TEXT)
                    new_node = TextNode(f'{string_list[i]}',TextType.TEXT)
                #if odd 1,3,5,....then TextType = text_type
                elif i%2 == 1:
                    #new_node = TextNode(f'"{string_list[i]}"',text_type)
                    new_node = TextNode(f'{string_list[i]}',text_type)
                list_of_new_nodes.append(new_node)
    
    return list_of_new_nodes

    '''
    Docstring for split_nodes_delimiter
    
    :param old_nodes: Description
    :param delimiter: Description
    :param text_type: Description

    example:
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.TEXT),
    ]

    '''