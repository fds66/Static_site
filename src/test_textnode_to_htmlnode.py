import unittest

from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node


class TestTextNode_to_HTMLNode(unittest.TestCase):

    def test_textnode_to_html_node_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_textnode_to_html_node_bold(self):
        node = TextNode("This is some test text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is some test text")

    def test_textnode_to_html_node_italic(self):
        node = TextNode("This is some test text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is some test text")

    def test_textnode_to_html_node_code(self):
            node = TextNode("This is some test text", TextType.CODE)
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "code")
            self.assertEqual(html_node.value, "This is some test text")
    
    def test_textnode_to_html_node_link(self):
            node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "a")
            self.assertEqual(html_node.value, "This is some anchor text")
            self.assertEqual(html_node.props,'{"href": "https://www.boot.dev",}')
    
    def test_textnode_to_html_node_images(self):
            node = TextNode("This is some anchor text", TextType.IMAGES, "https://www.boot.dev")
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "img")
            self.assertEqual(html_node.value, "")
            self.assertEqual(html_node.props,'{"src": "https://www.boot.dev", "alt": "This is some anchor text",}')
    
        

    '''
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_uneq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD,"http:/usr")
        node2 = TextNode("This is a text node", TextType.BOLD,"http:/usr")
        self.assertEqual(node, node2)

    def test_url_uneq_there_missing(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD,"http:/usr")
        self.assertNotEqual(node, node2)

    def test_url_uneq(self):
        node = TextNode("This is a text node", TextType.BOLD,"http:/src")
        node2 = TextNode("This is a text node", TextType.BOLD,"http:/usr")
        self.assertNotEqual(node, node2)

    def test_url_miss_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD,None)
        self.assertEqual(node, node2)

    def test_uneq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_exception_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            # This code runs, but the error is caught by the context manager
                parent_node.to_html()
    '''     




if __name__ == "__main__":
    unittest.main()