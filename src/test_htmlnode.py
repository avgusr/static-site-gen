import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_repr(self):
        node = HTMLNode(
            "p", "This is a paragraph", None, {"href": "https://www.google.com"}
        )
        self.assertEqual(
            "HTMLNode(p,This is a paragraph,None,{'href': 'https://www.google.com'})",
            repr(node),
        )


if __name__ == "__main__":
    unittest.main()
