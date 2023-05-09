import unittest
from pangolins import Node

class TestNode(unittest.TestCase):
    def test_properties(self):
        n = Node("test node", None)
        self.assertEqual(n.text, "test node", "node data unexpected")

    def test_leafness(self):
        parent = Node("parent", None)
        child  = Node("child", parent)
        self.assertFalse(parent.is_leaf, "root node cannot be leaf")


if __name__ == '__main__':
    unittest.main()



