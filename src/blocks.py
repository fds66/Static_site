
import textwrap
import re


from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"





####################################################
#Split blocks



def markdown_to_blocks(markdown):
    
    if len(markdown)<1 :
        raise Exception ("specified markdown is empty")
    list_blocks = []
    split_list = markdown.split("\n\n")
    for block in split_list:
        block = textwrap.dedent(block).strip()
        block = block.replace("\t","")
        if block == "":
            continue
        list_blocks.append(block)
    return list_blocks

def block_to_block_type(markdown_block):
    
    if len(markdown_block)<1 :
        raise Exception ("specified markdown block is empty")
    block_type = None
    
    # HEADINGS start with 1-6 # characters
    # multiline CODE blocks start with 3 backticks and a newline and end with 3 backticks
    # everyline in a QUOTE block starts with > , a space after > is allowed but not required
    # UNORDERED LIST every line must start with - followed by space
    # ORDERED LIST every line must start with a number followed by a full stop

    # PARAGRAPH is anything else that doesn't meet the above criteria

    
   # archive just in case
   # headings_pattern = r'(^#{1,6} )(.*)'
   # code_pattern = r'(^`{3}\n).*(`{3}$)' # with dotall single line s
   # quote_pattern = r'(^>).*' # do over each line
   # unordered_pattern = r'(^- ).*' # do over each line
   # ordered_pattern = r'(^\d+)(\. ).*' # do over each line
    #default is paragraph
   
        
    headings_pattern = block_type_to_regex(BlockType.HEADING)
    code_pattern = block_type_to_regex(BlockType.CODE)
    quote_pattern = block_type_to_regex(BlockType.QUOTE)
    unordered_pattern = block_type_to_regex(BlockType.UNORDERED_LIST)
    ordered_pattern = block_type_to_regex(BlockType.ORDERED_LIST)
    #default is paragraph

    
    heading_match = re.search(headings_pattern,markdown_block,re.DOTALL)
    #print(f"heading match {heading_match}")
    code_match = re.search(code_pattern,markdown_block,re.DOTALL)
    #print(f"code match {code_match}")

    #these methods need checking line by line so split it into line
    #markdown_lines = markdown_block.split("\n")
    markdown_lines = markdown_block.splitlines(keepends=True)
    #print(f"markdown_lines {markdown_lines}")
    #use a list of flags and check if all are true
    
    quote_flags = []
    unordered_flags = []
    ordered_flags=[]
        
    # a list to store the line numbers extracted from the ordered list
    ordered_lines=[]
    for line in markdown_lines:

        quote_match = re.search(quote_pattern,line)
        #print(f"quote match {quote_match}")
         
        quote_flags.append(bool(quote_match))
            

        unordered_match = re.search(unordered_pattern,line)
        #print(f"unordered match {unordered_match}")
        unordered_flags.append(bool(unordered_match))
            
            

        ordered_match = re.search(ordered_pattern,line)
        #print(f"ordered match {ordered_match}")
        ordered_flags.append(bool(ordered_match))
        if ordered_match:
            ordered_lines.append(ordered_match[1])
            

            
                
        #if it's an ordered list check the numbers start at one and increment by 1 each line
    check_flag = None
    if all(ordered_flags):
        for i in range(len(ordered_lines)):
            if i+1 == int(ordered_lines[i]) :
                check_flag = True
            else:
                check_flag = False
                break
                
    
    if heading_match:
        block_type = BlockType.HEADING
    elif code_match:
        block_type = BlockType.CODE
    elif all(quote_flags):
        block_type = BlockType.QUOTE
    elif all(unordered_flags):
        block_type = BlockType.UNORDERED_LIST
    elif all(ordered_flags) and check_flag:
        block_type = BlockType.ORDERED_LIST
    else:
        block_type = BlockType.PARAGRAPH
    


    return block_type

def block_type_to_regex(block_type):
    match block_type:

        case BlockType.CODE :
            regex_string = r'(^`{3}\n)(.*)(`{3}$)'


        case BlockType.HEADING:
            regex_string = r'(^#{1,6} )(.*)'

        case BlockType.QUOTE:
            regex_string = r'(^>)(.*)'

        case BlockType.UNORDERED_LIST :
            regex_string = r'(^- )(.*)'


        case BlockType.ORDERED_LIST:
            regex_string = r'(^\d+)(\. )(.*)'

        case _:
            raise Exception ("block_type not recognised in block_type to regex")

    return regex_string

