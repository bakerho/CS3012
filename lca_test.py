from binarytree import Node
import lca

class TestLca:

    def test_basic(self): #Test for basic case, nodes present in tree
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        lca1 = lca.findLCA(root, 4, 5)
        assert lca1.value is 2, "test_basic failed"

    def test_null(self): # Test case with empty tree
        root = None

        lca1 = lca.findLCA(root, 4, 5)
        assert lca1 is None, "test_null failed"

    
