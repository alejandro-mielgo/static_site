
class HTMLNode:
    
    def __init__(self, tag:str=None, value=None, children=None, props:dict=None)->None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self)->None:
        text:str = ""
        for key,value in self.props.items():
            text+=f'{key}="{value}" '
        return text.strip()
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
