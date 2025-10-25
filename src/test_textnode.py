import unittest

from textnode import TextNode, TextType
from textnode import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    # TextNode tests
    def test_eqTrue(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_eq2False(self):
        node = TextNode("This is a link", TextType.LINK, "http://example.com")
        node2 = TextNode("This is not a link", TextType.IMAGE, "http://example.com")
        self.assertNotEqual(node, node2)

    def test_eq3True(self):
        node = TextNode("This is a text node", TextType.ITALIC, "http://example.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "http://example.com")
        self.assertEqual(node, node2)
    
    #TextNode to HTMLNode conversion tests
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        bold_node = text_node_to_html_node(node)
        self.assertEqual(bold_node.tag, "b")
        self.assertEqual(bold_node.value, "This is a bold text node")

    def test_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        italic_node = text_node_to_html_node(node)
        self.assertEqual(italic_node.tag, "i")
        self.assertEqual(italic_node.value, "This is an italic text node")

    def test_code(self):
        node = TextNode("print('Hello, World!')", TextType.CODE)
        code_node = text_node_to_html_node(node)
        self.assertEqual(code_node.tag, "code")
        self.assertEqual(code_node.value, "print('Hello, World!')")

    def test_link(self):
        node = TextNode("Click here", TextType.LINK, "http://example.com")
        link_node = text_node_to_html_node(node)
        self.assertEqual(link_node.tag, "a")
        self.assertEqual(link_node.value, "Click here")
        self.assertEqual(link_node.props, {"href": "http://example.com"})

    def test_image(self):
        node = TextNode("An image", TextType.IMAGE, "http://example.com/image.png")
        image_node = text_node_to_html_node(node)
        self.assertEqual(image_node.tag, "img")
        self.assertEqual(image_node.value, "")
        self.assertEqual(image_node.props, {"src": "http://example.com/image.png", "alt": "An image"})
        

if __name__ == "__main__":
    unittest.main()