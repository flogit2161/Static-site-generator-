import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class HTMLNodeTest(unittest.TestCase):

    # HTMLNode tests

    def test_eq(self):
        node = HTMLNode(tag="div", value="Hello", props={"class": "greeting"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.props, {"class": "greeting"})
    # Need to add more tests here




    # LeafNode tests
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


   
   
   
   
   
   
   
   
   
    # ParentNode tests

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_node_with_props(self):
        child_node = LeafNode("p", "Hello")
        parent_node = ParentNode("div", [child_node], {"class": "container", "id": "main"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container" id="main"><p>Hello</p></div>'
        )

    def test_parent_node_multiple_children(self):
        child1 = LeafNode("p", "First")
        child2 = LeafNode("p", "Second")
        child3 = LeafNode("p", "Third")
        parent_node = ParentNode("div", [child1, child2, child3])
        self.assertEqual(
            parent_node.to_html(),
            "<div><p>First</p><p>Second</p><p>Third</p></div>"
        )



if __name__ == "__main__":
    unittest.main()