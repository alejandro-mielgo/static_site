from typing import Self

class HTMLNode:
    
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None)->None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other:Self)->bool:
        c1 = self.tag == other.tag
        c2 = self.value == other.value
        c3 = self.children == other.children
        c4 = self.props == self.props
        return c1 and c2 and c3 and c4
    
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self)->str:
        if self.props is not None:
            text:str = ""
            for key,value in self.props.items():
                text+=f'{key}="{value}" '
            return " "+text.strip()
        return ""
     
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'



class LeafNode(HTMLNode):
    def __init__(self,tag=None,value=None,props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")

        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"



class ParentNode(HTMLNode):

    def __init__(self,tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.children is None:
            raise ValueError('parent node must have children')
        if self.tag is None:
            raise ValueError('parent node must have a tag value')
        
        #call .to_html() recursively
        html:str = ""
        for child_node in self.children:
            html += child_node.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"
        
  

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

        
