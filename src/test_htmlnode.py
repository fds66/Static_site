import unittest

from htmlnode import HTMLNode

'''import unittest

def function_that_fails():
    raise ValueError("Oops!")

class TestExample(unittest.TestCase):
    def test_exception(self):
        # We tell the test runner we expect a ValueError
        with self.assertRaises(ValueError):
            # This code runs, but the error is caught by the context manager
            function_that_fails()'''



class TestHTMLNode(unittest.TestCase):
    
    
    def test_exception(self):
        # We tell the test runner we expect a ValueError
        with self.assertRaises(NotImplementedError):
            # This code runs, but the error is caught by the context manager
           
            node = HTMLNode()
            node.to_html()
        
    
    def test_repr(self):
        node = HTMLNode("p","Node 1")
        result = node.__repr__()
        expected = "HTMLNode(p, Node 1, None, None)"
        self.assertEqual(result,expected)
     
    def test_props_to_html(self):
        props = {"href": "https://www.google.com","target": "_blank",}
        node = HTMLNode("p","this is the text",None,props)
        result = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'    
        self.assertEqual(result, expected)
      
    def test_props_to_html_blank(self):
        
        node = HTMLNode()
        result = node.props_to_html()
        expected = ""    
        self.assertEqual(result, expected)

        




if __name__ == "__main__":
    unittest.main()