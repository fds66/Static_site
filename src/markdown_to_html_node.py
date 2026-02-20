from enum import Enum
import pprint
import re
import textwrap

from textnode import TextNode, TextType
from htmlnode import HTMLNode,LeafNode,ParentNode
from textnode_to_htmlnode import text_node_to_html_node
from split_nodes import split_nodes_delimiter,split_nodes_link,split_nodes_image
from extract_markdown import extract_markdown_images,extract_markdown_links
from text_to_textnodes import text_to_textnodes
from blocks import markdown_to_blocks,block_to_block_type,BlockType,block_type_to_regex








def markdown_to_html_node(markdown):
    #split the markdown into blocks
    block_list = markdown_to_blocks(markdown)
    block_node_list = []

    #for each block determine the type of block
    for markdown_block in block_list:
        #what type of block?
        block_type = block_to_block_type(markdown_block)

        #create new html node with the correct data
        tag = block_type_to_tag(block_type,markdown_block)
        block_node = ParentNode(tag,None)

        #assign the proper child html node objects to the the block node
        #shared text_to_chidren(text) that works for all block types except code
        if block_type == BlockType.CODE:
            

            #code block is special case where you don't do inline parsing. Manuallly made textnode and used text_node_to_html_node
            #text in, strip ``` from string, make text into text node, convert to leaf node, add as child to code node, create outer node to add pre and code node as child
            # just in case r'(^`{3}\n)(.*)(`{3}$)'

            code_pattern = block_type_to_regex(BlockType.CODE)
            code_match = re.search(code_pattern,markdown_block,re.DOTALL)
            text = code_match[2]
            text = text.replace("\n","<br>")
            code_text_node = TextNode(text,TextType.TEXT)
            child_nodes = text_node_to_html_node(code_text_node)
            block_node.children = [child_nodes]
            outer_pre_node = ParentNode("pre",[block_node])
            block_node_list.append(outer_pre_node)
            
        else:
            
            child_nodes = text_to_children(markdown_block,block_type)
            block_node.children = child_nodes
            block_node_list.append(block_node)

        
        


    #Make all the block nodes children under a single parent html node(which should justs be a div) adn return it
    final_parent = ParentNode("div",block_node_list)
    #the final parent puts <div>........</div> just a parent node with tag "div"
    
    
    
    return final_parent



def block_type_to_tag(block_type,block_text):
    if  block_type not in BlockType:
        raise Exception ("block_type is not part of the BlockType enum")
    
        
    match block_type:

        case BlockType.PARAGRAPH:
            return "p"

        case BlockType.HEADING:
            #tag depends on how many #
            #if one # h1, two ## h2 etc up to h6
            number_hashes = 0
            for i in range(6):
                if block_text[i] == "#":
                    number_hashes+=1
            heading_tag = f"h{number_hashes}"
            return heading_tag

        case BlockType.CODE:
            return "code"
            
        case BlockType.QUOTE:
            return "blockquote"

        case BlockType.UNORDERED_LIST:
            return "ul"

        case BlockType.ORDERED_LIST:
            return "ol"
        
           
        case _:
            result = f"no known blocktype selected"
            return result

    return tag

def text_to_children(text,block_type):
    #takes a string of text and returns a list of html nodes that represent the 
    #inline markdown using previously created functions (think textnode to htmlnode)

    # NOTE to self: deal with blank space and tabs

    match block_type:

        
            #deal with the newlines, for paragraph remove, for quote change to html line break, for heading remove and remove the ##

            
        case BlockType.PARAGRAPH :
            text = text.replace("\n"," ")
            child_nodes = text_to_textnodes(text)
            #convert the child text nodes into html leaf nodes and add them to the child_html_nodes list
            child_html_nodes = child_nodes_to_leaf_nodes(child_nodes)
            return child_html_nodes
            
        case BlockType.HEADING :
            text = text.replace("\n"," ")
            headings_pattern = block_type_to_regex(BlockType.HEADING)
            heading_match = re.search(headings_pattern,text,re.DOTALL)
            #capture group 2 contains the body minus the hashes
            text = heading_match[2]
            child_nodes = text_to_textnodes(text)
            #convert the child text nodes into html leaf nodes and add them to the child_html_nodes list
            child_html_nodes = child_nodes_to_leaf_nodes(child_nodes)
            return child_html_nodes


        case BlockType.QUOTE :
            text = text.replace("\n","<br>")
            child_nodes = text_to_textnodes(text)
            #convert the child text nodes into html leaf nodes and add them to the child_html_nodes list
            child_html_nodes = child_nodes_to_leaf_nodes(child_nodes)
            return child_html_nodes
        
        # deal with the lists
        #for unordered  and ordered lists each line needs separate tag of "li"
        # remove the numbers for ordered and the  dashes for unordered (check if spaces need to be in or not)

        case BlockType.UNORDERED_LIST :
            text_lines = text.split("\n")
            line_nodes = []

            for line in text_lines:
                line = textwrap.dedent(line).strip()
                line = line.replace("\t","")
                line_contents = re.search(block_type_to_regex(BlockType.UNORDERED_LIST),line)
                #capture group 2 contains the body minus the dashes
                line = line_contents[2]
                child_nodes = text_to_textnodes(line)
                child_html_nodes = child_nodes_to_leaf_nodes(child_nodes)
                parent_node = ParentNode("li",child_html_nodes)
                line_nodes.append(parent_node)
            return line_nodes
            

        case BlockType.ORDERED_LIST :

            text_lines = text.split("\n")
            line_nodes = []
           
            for line in text_lines:
                line = textwrap.dedent(line).strip()
                line = line.replace("\t","")
                line_contents = re.search(block_type_to_regex(BlockType.ORDERED_LIST),line)
                #capture group 3 contains the body minus the numbers (we created an extra group so we could test if the numbers were consecutive)
                line = line_contents[3]
                child_nodes = text_to_textnodes(line)
                child_html_nodes = child_nodes_to_leaf_nodes(child_nodes)
                parent_node = ParentNode("li",child_html_nodes)
                line_nodes.append(parent_node)
            return line_nodes
        




        
def child_nodes_to_leaf_nodes(child_nodes):
    child_html_nodes = []
    for child in child_nodes:
        child_html_node = text_node_to_html_node(child)
        child_html_nodes.append(child_html_node)
    return child_html_nodes




    
   
    
    
    
   


