import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("this is a text node", TextType.BOLD)
        self.assertIsNone(node.url, "URL on TextNode should default to None")

    def test_eq_negative(self):
        bold_node = TextNode("This is a text node", TextType.BOLD)
        italic_node = TextNode("This is an italic node", TextType.ITALIC)
        self.assertNotEqual(bold_node, italic_node)

    def test_url_populates(self):
        url_node = TextNode("This is a url node", TextType.LINK, "https://boot.dev")
        self.assertIsNotNone(url_node.url)


if __name__ == "__main__":
    unittest.main()
