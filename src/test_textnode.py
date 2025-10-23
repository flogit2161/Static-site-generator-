import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
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
    

if __name__ == "__main__":
    unittest.main()