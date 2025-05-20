import unittest

from htmlnode import HTMLNode


class TestHMLNode(unittest.TestCase):

    def test_repr(self):
        node = HTMLNode('a', 'este es el valor', None, {'class':'active', 'target':'_blank'})
        self.assertEqual("HTMLNode(a, este es el valor, None, {'class': 'active', 'target': '_blank'})", str(node))

    def test_props_to_html(self):
        node = HTMLNode('a', 'este es el valor', None, {'class':'active', 'target':'_blank'})
        self.assertEqual('class="active" target="_blank"', node.props_to_html())


if __name__ == '__main__':
    unittest.main()