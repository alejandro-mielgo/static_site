from enum import Enum
from typing import Self

from htmlnode import LeafNode

class TextType(Enum):
    TEXT = 'text'
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    
    def __init__(self, text:str, text_type:str, url:str=None)->None:
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other:Self):
        c1 = self.text == other.text
        c2 = self.text_type == other.text_type
        c3 = self.url == other.url
        return c1 and c2 and c3

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


# class LeafNode(HTMLNode):
#     def __init__(self,tag,value,props=None):

def text_node_to_html_node(text_node:TextNode) -> LeafNode:
    
    match text_node.text_type:
        
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        
        case TextType.BOLD:
            return LeafNode(tag="b",value=text_node.text)

        case TextType.ITALIC:
            return LeafNode(tag="i",value=text_node.text)

        case TextType.CODE:
            return LeafNode(tag="code",value=text_node.text)

        case TextType.LINK:
            return LeafNode(tag="a",value=text_node.text)

        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props = {"src":text_node.url, "alt":text_node.text})
        
        case _:
            raise ValueError('ERROR: wrong type of text type')