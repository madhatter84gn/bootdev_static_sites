import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This text is different", "bol")
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This text is the same", "bold")
        node2 = TextNode("This text is the same", "italic")
        self.assertNotEqual(node, node2)

    def test_repr_text(self):
        node = TextNode("This is a text node",
                        text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)",
            repr(node)
        )

    def test_repr_text_bold(self):
        node = TextNode("This is a text node",
                        text_type_bold, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, bold, https://www.boot.dev)",
            repr(node)
        )


if __name__ == "__main__":
    unittest.main()
