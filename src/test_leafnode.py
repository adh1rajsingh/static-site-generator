import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')
    
    def test_to_html_2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_(self):
        node = LeafNode("a", "Click me!", {"title": "Testing", "href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a title="Testing" href="https://www.google.com">Click me!</a>')

    def test_empty_value_raises_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()
    


if __name__ == "__main__":
    unittest.main()