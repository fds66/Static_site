import unittest

from htmlnode import ParentNode,LeafNode,HTMLNode

'''import unittest

def function_that_fails():
    raise ValueError("Oops!")

class TestExample(unittest.TestCase):
    def test_exception(self):
        # We tell the test runner we expect a ValueError
        with self.assertRaises(ValueError):
            # This code runs, but the error is caught by the context manager
            function_that_fails()'''



class TestParentNode(unittest.TestCase):
    
    
    def test_exception_no_child(self):
        # We tell the test runner we expect a ValueError
        with self.assertRaises(ValueError):
            # This code runs, but the error is caught by the context manager
           
            node = ParentNode("a",None)
            node.to_html()
            
       
    
    def test_exception_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            # This code runs, but the error is caught by the context manager
                parent_node.to_html()
       
    
    def test_repr(self):
        node = ParentNode("p",[LeafNode("b","This is a leaf")])
        result = node.__repr__()
        expected = "ParentNode(p, [LeafNode(b, This is a leaf, None)], None)"
        self.assertEqual(result,expected)
    
    def test_props_to_html(self):
        props = {"href": "https://www.google.com","target": "_blank",}
        node = ParentNode("p",LeafNode("b","Text"),props)
        result = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'    
        self.assertEqual(result, expected)
      
    def test_props_to_html_blank_props(self):
        
        
        result = ParentNode("p",LeafNode("b","Text")).props_to_html()
        expected = ""   
        self.assertEqual(result, expected)

    
    
        #tests given to us

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_nested_parent(self):
         
        node = ParentNode("p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ParentNode("a",[LeafNode("b","Nested parent")])
        ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<a><b>Nested parent</b></a></p>",
        )


if __name__ == "__main__":
    unittest.main()













