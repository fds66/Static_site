
import textwrap


'''
example
Input:
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item

Output:
string 1:
# This is a heading
string 2:
This is a paragraph of text. It has some **bold** and _italic_ words inside of it.
string 3:
- This is the first list item in a list block
- This is a list item
- This is another list item

'''








def markdown_to_blocks(markdown):
    list_blocks = []
    split_list = markdown.split("\n\n")
    for block in split_list:
        block = textwrap.dedent(block).strip()
        block = block.replace("\t","")
        if block == "":
            continue
        list_blocks.append(block)
    return list_blocks
    