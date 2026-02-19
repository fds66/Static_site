import re


#takes raw markdown text and returns a list of tuples. 
#Each tuple should contain the alt text and url of any markdown images

'''
examples
text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
# 

test example :
def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
# 
'''

def extract_markdown_images(text):
    regex_exp = r'(\[(.*?)\]\((.*?)\))'
    matches = re.findall(regex_exp,text)
    output_list = []
    for match in matches:
        alt = match[1]
        url = match[2]
        output_list.append((alt,url))
       # print (match)
       # print(f"alt = {alt}, url = {url}")
    return output_list



#takes a markdown text and extract markdown links.
#returns tuples of anchor text and urls
'''
example
text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
print(extract_markdown_links(text))
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]


'''

def extract_markdown_links(text):
    regex_exp = r'(\[(.*?)\]\((.*?)\))'
    matches = re.findall(regex_exp,text)
    output_list = []
    for match in matches:
        anchor_text = match[1]
        url = match[2]
        output_list.append((anchor_text,url))
       # print (match)
       # print(f"alt = {alt}, url = {url}")
    return output_list

