from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")

        if self.tag is None:
            return value
        
        return f"<{self.tag}>{self.value}</{self.tag}>"