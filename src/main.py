from enum import Enum
import pprint
from textnode import TextNode, TextType
from htmlnode import HTMLNode,LeafNode,ParentNode
from textnode_to_htmlnode import text_node_to_html_node
from split_nodes import split_nodes_delimiter,split_nodes_link,split_nodes_image
from extract_markdown import extract_markdown_images,extract_markdown_links
from text_to_textnodes import text_to_textnodes
from blocks import markdown_to_blocks,block_to_block_type
from markdown_to_html_node import markdown_to_html_node




def main():
    print("running main")

    
    md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """
    
    #md = """
    #1. Make food
    #2. Feed the dog
    #3. Go for a walk
    #"""

    #md="""
    #- prepare a lesson
    #- ace the tests
    #- go on to the next lesson
    #"""






    '''
    md = """
    ### This is the heading number 3
    """

    md = """
    > This is to quote a poem from a poet\n> when I see a daffodil\n> I write a poem about it"""

    
    md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """
    

    md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """
    '''
    node = markdown_to_html_node(md)
    #print(node)
    html = node.to_html()
    print(html)









    #text = """### this is a heading"""
    #text = """>tommorow is another day\n>what will I do?"""
    #text = """- must do this\n- must do that"""
    #text = """1. this is an ordered list\n2. what will happen?\n3. who knows"""
    #text = """```\nthis is a code block```"""
    #text = """1. do the dishes\n2. clean the floor"""
    #text = """some randowm text```"""
    #print(text)
    #block_type = block_to_block_type(text)
    #print(block_type)





    '''       
    md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
    blocks = markdown_to_blocks(md)
    pprint.pprint(blocks)
    
    print(blocks)

    '''
    '''expecting
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        


    
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    result = text_to_textnodes(text)
    pprint.pprint(result)
    
  
    #text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    #result = extract_markdown_images(text)
    #print(result)


    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    #print(extract_markdown_links(text))
    node = TextNode(text,TextType.LINK)
    result = split_nodes_link([node])
    print(result)

   
    text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)"
    #print(extract_markdown_links(text))
    node = TextNode(text,TextType.IMAGE)
    result = split_nodes_image([node])
    print()
    print()
    print(result)
    '''
    '''

    node = TextNode("This is text with an _italic_ word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.ITALIC)
    print(new_nodes)   


   
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