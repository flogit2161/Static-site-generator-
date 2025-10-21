from enum import Enum

class TextNodeType(Enum):
    TEXT_PLAIN = "text(plain)"
    TEXT_BOLD = "**Bold text**"
    TEXT_ITALIC = "*_Italic text_*"
    CODE_TEXT = "`Code text`"
    LINK_TEXT = "[anchor text](url)"
    IMAGE_TEXT = "![alt text](url)"


class TextNode:
    def __init__(self, text, text_type: TextNodeType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self):
        return f"TextNode(TEXT={self.text}, TEXT_TYPE={self.text_type.value}, URL={self.url})"
    



