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

    def test_convert_text_to_html_node(self):
        node = TextNode("Plain text", TextType.TEXT)
        html_node = node.convert_to_html_node()
        self.assertEqual(html_node.to_html(), "Plain text")

    def test_convert_bold_to_html_node(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = node.convert_to_html_node()
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    def test_convert_italic_to_html_node(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = node.convert_to_html_node()
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    def test_convert_code_to_html_node(self):
        node = TextNode("code snippet", TextType.CODE)
        html_node = node.convert_to_html_node()
        self.assertEqual(html_node.to_html(), "<code>code snippet</code>")

    def test_convert_link_to_html_node(self):
        node = TextNode("Click here", TextType.LINK, "https://boot.dev")
        html_node = node.convert_to_html_node()
        self.assertEqual(
            html_node.to_html(),
            '<a href="https://boot.dev" target="_blank">Click here</a>',
        )

    def test_convert_image_to_html_node(self):
        node = TextNode("Image description", TextType.IMAGE, "https://example.com/image.png")
        html_node = node.convert_to_html_node()
        self.assertEqual(
            html_node.to_html(),
            '<img src="https://example.com/image.png" alt="Image description"></img>',
        )


if __name__ == "__main__":
    unittest.main()
