import unittest

from htmlnode import LeafNode

'''import unittest

def function_that_fails():
    raise ValueError("Oops!")

class TestExample(unittest.TestCase):
    def test_exception(self):
        # We tell the test runner we expect a ValueError
        with self.assertRaises(ValueError):
            # This code runs, but the error is caught by the context manager
            function_that_fails()'''



class TestLeafNode(unittest.TestCase):
    
    '''
    def test_exception(self):
        # We tell the test runner we expect a ValueError
        with self.assertRaises(NotImplementedError):
            # This code runs, but the error is caught by the context manager
           
            node = HTMLNode()
            node.to_html()
    '''    
    
    def test_repr(self):
        node = LeafNode("p","Node 1")
        result = node.__repr__()
        expected = "LeafNode(p, Node 1, None)"
        self.assertEqual(result,expected)
     
    def test_props_to_html(self):
        props = {"href": "https://www.google.com","target": "_blank",}
        node = LeafNode("p","this is the text",props)
        result = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'    
        self.assertEqual(result, expected)
      
    def test_props_to_html_blank_props(self):
        
        node = LeafNode("p","this is the text")
        result = node.props_to_html()
        expected = ""   
        self.assertEqual(result, expected)

    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        result = node.to_html()
        expected = '<p>This is a paragraph of text.</p>'   
        self.assertEqual(result, expected)
 
    def test_to_html_with_props(self):
        
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = node.to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'   
        self.assertEqual(result, expected)
 
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")



if __name__ == "__main__":
    unittest.main()