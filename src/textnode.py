from enum import Enum
from typing import Self

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    ANCHOR = "anchor"
    IMAGE =  "image"


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

