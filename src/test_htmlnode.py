import unittest

from htmlnode import HTMLNode

class HTMLNodeTest(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="div", value="Hello", props={"class": "greeting"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.props, {"class": "greeting"})
    # Need to add more tests here


if __name__ == "__main__":
    unittest.main()