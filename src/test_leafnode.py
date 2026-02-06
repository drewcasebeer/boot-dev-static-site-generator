import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_repr_is_correct(self):
        leaf_node = LeafNode("p", "Some text")
        result = "LeafNode(p, Some text, None)"
        self.assertEqual(leaf_node.__repr__(), result)

    def test_html_empty_value(self):
        leaf_node = LeafNode("p", None)

        try:
            leaf_node.to_html()
            self.assertEqual(1, 2, "An error should have occured")
        except ValueError:
            return

    def test_html_empty_tag(self):
        leaf_node = LeafNode(None, "Some text")
        self.assertEqual(leaf_node.to_html(), "Some text")

    def test_html_without_props(self):
        leaf_node = LeafNode("p", "Some text")
        result = "<p>Some text</p>"
        self.assertEqual(leaf_node.to_html(), result)

    def test_html_with_props(self):
        leaf_node = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        result = '<a href="https://www.google.com">Click Me!</a>'
        self.assertEqual(leaf_node.to_html(), result)
