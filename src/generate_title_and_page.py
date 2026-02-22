from enum import Enum
import pprint
import os
import shutil
import re


from textnode import TextNode, TextType
from htmlnode import HTMLNode,LeafNode,ParentNode
from textnode_to_htmlnode import text_node_to_html_node
from split_nodes import split_nodes_delimiter,split_nodes_link,split_nodes_image
from extract_markdown import extract_markdown_images,extract_markdown_links
from text_to_textnodes import text_to_textnodes
from blocks import markdown_to_blocks,block_to_block_type
from markdown_to_html_node import markdown_to_html_node
from copy_from_sourece_dir_to_dest_dir import copy_source_dir_to_dest_dir



def extract_title(markdown):
    if markdown == "":
        raise Exception ("Empty markdown sent to extract_title")
    #note I used regex again, could have used .startswith()
    # pull the h1 header - line begins with #
    lines = markdown.split("\n")
    for line in lines:
        line = line.strip()
        #print(line)
        #print(f"line {line}")
        poss_title = re.search(r'(^# )(.*)',line)
        
            
        if poss_title:
            #print(f" whole {poss_title},zero {poss_title[0]}, one {poss_title[1]}, two {poss_title[2]}")
            return poss_title[2]


    
    if not poss_title:
        raise Exception ("No h1 title found")




def generate_page(from_path, template_path, dest_path, basepath):
    #print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    try:
        with open(from_path,"r") as f:
            content = f.read()
    except Exception as e:
        raise Exception (f"{from_path} cannot be read, error {e}")
    
    try:
        with open(template_path) as g:
            template = g.read()
    except Exception as e:
        raise Exception (f"{template_path} cannot be read, error {e}")
    
    # process the markdown content into html
    html_nodes = markdown_to_html_node(content)
    #pprint.pprint(f"html nodes {html_nodes}")
    html_content = html_nodes.to_html()
    #print (html_content)
    #extract the title
    title = extract_title(content)

    #insert the title and contents into the template 
    full_html = template.replace("{{ Title }}",title)
    full_html = full_html.replace("{{ Content }}",html_content)
    new_href_str = f'href="{basepath}'
    full_html = full_html.replace('href="/',new_href_str)
    new_src_str = f'src="{basepath}'
    full_html = full_html.replace('src="/',new_src_str)
    
    #print(full_html)

    #If the destination doesn't exist then create it
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, 'w') as file:
            file.write(full_html)
            return


    except Exception as e:
        raise Exception ("writing to the file failed")
    


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_list = os.listdir(dir_path_content)
    print(content_list)

    #crawl every entry in the content directory

    for item in content_list:
        item_path = os.path.join(dir_path_content,item)
        dest_path = os.path.join(dest_dir_path,item)
        if os.path.isfile(item_path):
            print (f"{item} is a file")
            file_name, file_extension = os.path.splitext(item)
            if file_extension == ".md":
                print ("this is a markdown file")
                print(f"new file will be {file_name} with .html added")
                html_file_name = file_name + ".html"
                html_file_path = os.path.join(dest_dir_path,html_file_name)
                print (html_file_name, html_file_path)
                generate_page(item_path,template_path, html_file_path, basepath)
            else:
                continue
        if os.path.isdir(item_path):
            print(f"{item} is a directory")
            print(f"destination path is {dest_path}")
            generate_pages_recursive(item_path, template_path, dest_path, basepath)
    #for each markdown file found, generate a new .html file using the same template
    #write the generated pages to the public directory in the same directory structure
    #generate_page(from_path, template_path, dest_path)


