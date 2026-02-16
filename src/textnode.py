from enum import Enum

class TextType(Enum):
    PLAIN = "text(plain)"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "'Code text'"
    LINK = "[anchor text](url)"
    IMAGES = "![alt text](url)"

class TextNode():
    def __init__(self,text,text_type: TextType,url=None):
        self.text = text
        
        self.text_type = text_type
        self.url = None
        if url:
            self.url = url
        
           

    def __eq__(self,other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
            
