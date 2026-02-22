import unittest
from generate_title_and_page import generate_page, extract_title

class TestGenerateTitleAndPage(unittest.TestCase):

    def test_extract_title(self):
        md = """
        # This is the title Hello

        ### this is a subtitle

        this is a normal paragraph
        """
    
        
        self.assertEqual(extract_title(md),"This is the title Hello")

    def test_extract_title_empty(self):

        with self.assertRaises(Exception): 
            md = "" 
            extract_title(md) 


    


if __name__ == "__main__":
    unittest.main()