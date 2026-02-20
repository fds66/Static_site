import unittest
from extract_markdown import extract_markdown_images,extract_markdown_links
from blocks import markdown_to_blocks, block_to_block_type,BlockType






class Test_markdown_to_blocks(unittest.TestCase):

    

    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_markdown_to_blocks_extra_newlines(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line






        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_example_course(self):
        md = """
        # This is a heading

        This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

        - This is the first list item in a list block
        - This is a list item
        - This is another list item
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
              "# This is a heading" ,
              "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
              "- This is the first list item in a list block\n- This is a list item\n- This is another list item",
            ],
        )



    def test_block_to_block_type_heading(self):

        markdown = """### this is a heading"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type,BlockType.HEADING)

    def test_block_to_block_type_quote(self):

        markdown = """>tommorow is another day\n>what will I do?"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type,BlockType.QUOTE)

    def test_block_to_block_type_unordered(self):

        markdown = """- must do this\n- must do that"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type,BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered(self):

        markdown = """1. this is an ordered list\n2. what will happen?\n3. who knows"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type,BlockType.ORDERED_LIST)

    def test_block_to_block_type_code(self):

        markdown = """```\nthis is a code block```"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type,BlockType.CODE)

    def test_block_to_block_type_code_text_before(self):

        markdown = """some randowm text```"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type,BlockType.PARAGRAPH)

    def test_block_to_block_type_heading_no_space(self):

        markdown = """###this is a heading"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type,BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_no_space(self):

        markdown = """-must do this\n- must do that"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type,BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_no_space(self):

        markdown = """1.this is an ordered list\n2. what will happen?\n3. who knows"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type,BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_not_sequential(self):

        markdown = """1. this is an ordered list\n3. what will happen?\n3. who knows"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type,BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_missing_number(self):

        markdown = """1. this is an ordered list\nwhat will happen?\n3. who knows"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type,BlockType.PARAGRAPH)

    def test_block_to_block_type_empty_input_exception(self):
        with self.assertRaises(Exception):
            markdown = ""
            block_type = block_to_block_type(markdown)
        







if __name__ == "__main__":
    unittest.main()