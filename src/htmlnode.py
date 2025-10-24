class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children 
        self.props = props 

    def to_html(self):
        raise NotImplementedError("Not Implemented yet")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
        return props_str
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value to convert to HTML")
        if self.tag is None:
            return self.value
        props_str = self.props_to_html()
        start_tag = f"<{self.tag}{props_str}>"
        end_tag = f"</{self.tag}>"
        return f"{start_tag}{self.value}{end_tag}"
        


