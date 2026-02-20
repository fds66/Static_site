import unittest

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


class Test_markdown_to_html_node(unittest.TestCase):

    def test_markdown_to_html_node(self):
        pass


    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain<br>the **same** even with inline stuff<br></code></pre></div>",
        )
    def test_quoteblock(self):
        md = """> This is to quote a poem from a poet\n> when I see a daffodil\n> I write a poem about it"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><blockquote>> This is to quote a poem from a poet<br>> when I see a daffodil<br>> I write a poem about it</blockquote></div>"
        self.assertEqual(html,expected)

    def test_headingblock(self):
        md = """### This is the heading number 3"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><h3>This is the heading number 3</h3></div>"
        self.assertEqual(html,expected)

    def test_ordered_block(self):
        md = """ 1. Make food\n2. Feed the dog\n3. Go for a walk"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><ol><li>Make food</li><li>Feed the dog</li><li>Go for a walk</li></ol></div>"
        self.assertEqual(html,expected)

    def test_unorderedblock(self):
        md = """- prepare a lesson\n- ace the tests\n- go on to the next lesson"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><ul><li>prepare a lesson</li><li>ace the tests</li><li>go on to the next lesson</li></ul></div>"
        self.assertEqual(html,expected)

    def test_ordered_block_separate_lines(self):
        md = """ 
        1. Make food
        2. Feed the dog
        3. Go for a walk"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><ol><li>Make food</li><li>Feed the dog</li><li>Go for a walk</li></ol></div>"
        self.assertEqual(html,expected)

    def test_unorderedblock(self):
        md = """
        - prepare a lesson
        - ace the tests
        - go on to the next lesson"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><ul><li>prepare a lesson</li><li>ace the tests</li><li>go on to the next lesson</li></ul></div>"
        self.assertEqual(html,expected)
    











if __name__ == "__main__":
    unittest.main()


