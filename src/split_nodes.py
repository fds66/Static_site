from enum import Enum
import pprint
from textnode import TextType,TextNode
from htmlnode import HTMLNode,LeafNode,ParentNode
from extract_markdown import extract_markdown_images,extract_markdown_links
import re

# reminder of enum types
'''class TextType(Enum):
    TEXT = "text(plain)"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "'Code text'"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"
    
    
    class TextNode():
    def __init__(self,text,text_type: TextType,url=None):
 
 '''





def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #print("running split nodes delimiter")
    list_of_new_nodes =[]
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            list_of_new_nodes.append(old_node)
            continue
        
        string_list = old_node.text.split(delimiter)
        
        if len(string_list)%2 == 0:
            raise ValueError ("Invalid Markdown syntax, closing delimiter not found")

        for i in range(len(string_list)):
            #if an empty string then skip it
            if string_list[i] == "":
                continue
            #if even 0,2,4,...then TextType.TEXT
            if i%2 == 0:
                #new_node = TextNode(f'"{string_list[i]}"',TextType.TEXT)
                new_node = TextNode(string_list[i],TextType.TEXT)
                #if odd 1,3,5,....then TextType = text_type
            elif i%2 == 1:
                #new_node = TextNode(f'"{string_list[i]}"',text_type)
                new_node = TextNode(string_list[i],text_type)
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
##################################################################################
'''
Usage
node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_link([node])
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]




'''





def split_nodes_link(old_nodes):
    #print("running split nodes link")
    #print(old_nodes)
    list_of_new_nodes =[]

    for old_node in old_nodes:
        #print(old_node)
        #print(old_node.text)
        if old_node.text_type != TextType.TEXT:
            list_of_new_nodes.append(old_node)
            continue
        
        string = old_node.text
        
        #get the link details from extracting function
        link_results = extract_markdown_links(string)
        #print(f"link_results {link_results}")
        #track link_results using a different index j
        j = 0
            
        
        pattern = r'(\[.*?\]\(.*?\))'

        string_list = re.split(pattern,string)
        #for i in range(len(string_list)):
            #print(f"string list {i} : {string_list[i]}")
        
        for i in range(len(string_list)):
            #print(f"loop {i} string_list[i] = {string_list[i]}")
            if string_list[i] == "":
                continue
                
                #even number string are text
            if i%2 == 0:
                new_text_node = TextNode(string_list[i],TextType.TEXT)
                list_of_new_nodes.append(new_text_node)

                #odd number strings are links:
            if i%2 == 1:
                if j<len(link_results):
                    #print(f" link_results[j],link_results[j][0],link_results[j][1]  {link_results[j]},{link_results[j][0]},{link_results[j][1]}")
                    new_link_node = TextNode(link_results[j][0],TextType.LINK,link_results[j][1])
                    list_of_new_nodes.append(new_link_node)
                    j+=1
            #print(list_of_new_nodes)
        #print(list_of_new_nodes)
                         
    return list_of_new_nodes
###########################################################################################################

def split_nodes_image(old_nodes):
    #print("running split nodes image")
    #print(old_nodes)
    
    list_of_new_nodes =[]
    for old_node in old_nodes:
        #print(old_node)
        #print(f" original text {old_node.text}")
        if old_node.text_type != TextType.TEXT:
            list_of_new_nodes.append(old_node)
            continue
        
        string = old_node.text
                
        images_results = extract_markdown_images(string)
        #track image results using a different index j
        j=0
         
        pattern = r'(\!\[.*?\]\(.*?\))'
        string_list = re.split(pattern,string)
        #for i in range(len(string_list)):
            #print(f"string list {i} : {string_list[i]}")


        #print(string_list)

        for i in range(len(string_list)):
            #print(f"loop {i} string_list[i] = {string_list[i]}")
            if string_list[i] == "":
                continue
                
                #even number string are text
            if i%2 == 0:
                new_text_node = TextNode(string_list[i],TextType.TEXT)
                list_of_new_nodes.append(new_text_node)

                #odd number strings are images:
            if i%2 == 1:
                if j<len(images_results):
                    new_image_node = TextNode(images_results[j][0],TextType.IMAGE,images_results[j][1])
                    list_of_new_nodes.append(new_image_node)
                    j+=1
                               
    return list_of_new_nodes