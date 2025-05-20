from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self,tag,children,props=None):
        super().__init__(self, tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.children is None:
            raise ValueError('parent node must have children')
        if self.tag is None:
            raise ValueError('parent node must have a tag value')

        
