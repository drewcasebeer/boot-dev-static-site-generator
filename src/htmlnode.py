class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This method has not been implemented yet")

    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""

        result = ""
        for key in self.props:
            result += f' {key}="{self.props[key]}"'

        return result

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"
