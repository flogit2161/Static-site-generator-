import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
class HTMLNodeTest(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="div", value="Hello", props={"class": "greeting"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.props, {"class": "greeting"})
    # Need to add more tests here

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()