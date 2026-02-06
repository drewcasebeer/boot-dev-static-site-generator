import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_print(self):
        html_node = HTMLNode(
            "a",
            "value",
            "children",
            {"href": "https://www.google.com", "target": "_blank"},
        )
        result = "HtmlNode(a, value, children, {'href': 'https://www.google.com', 'target': '_blank'})"

        self.assertEqual(html_node.__repr__(), result)

    def test_no_props_returns_empty_string(self):
        html_node = HTMLNode()
        self.assertEqual(html_node.props_to_html(), "")

    def test_empty_props_returns_empty_string(self):
        html_node = HTMLNode(None, None, None, {})
        self.assertEqual(html_node.props_to_html(), "")

    def test_props(self):
        html_node = HTMLNode(
            None, None, None, {"href": "https://www.google.com", "target": "_blank"}
        )
        props_string = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(html_node.props_to_html(), props_string)
