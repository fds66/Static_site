from enum import Enum
import pprint
import os
import shutil


from textnode import TextNode, TextType
from htmlnode import HTMLNode,LeafNode,ParentNode
from textnode_to_htmlnode import text_node_to_html_node
from split_nodes import split_nodes_delimiter,split_nodes_link,split_nodes_image
from extract_markdown import extract_markdown_images,extract_markdown_links
from text_to_textnodes import text_to_textnodes
from blocks import markdown_to_blocks,block_to_block_type
from markdown_to_html_node import markdown_to_html_node
from copy_from_sourece_dir_to_dest_dir import copy_source_dir_to_dest_dir




def main():
    print("running main")

    #copy everything from static to public

    source_directory = "./static"   
    destination_directory = "./public"
    #if the destination directory already exists delete it and all its contents
    if os.path.exists(destination_directory):
        print("deleting public directory")
        rmtree_result = shutil.rmtree(destination_directory)
        print(rmtree_result)
    copy_source_dir_to_dest_dir(source_directory,destination_directory)
    return

    
main()