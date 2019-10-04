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

    def test_nonpresent_node(self): # Test case for a node not present in tree
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        lca1 = lca.findLCA(root, 4, 8)
        assert lca1 is None, "test_nonpresent_node failed"

        node1 = lca.find(root,4) #Test each node indivdually
        assert node1 is True, "test_nonpresent_node node1 failed"
        node2 = lca.find(root,8)
        assert node2 is False, "test_nonpresent_node node1 failed"

    #def test_root_node(self):# Test case where root is a node of interest for lca

    #def test_lowest_ndde (self): # Test case with one of the lowest nodes in tree

    #def test_left_right_node (self): # Test case with one node in the furthest left tree and the other in the furthest right tree

    #def test_two_nodes_with_equal_keys(self): # Test case with two nodes of equal keys

    #def test_three_nodes_with_equal_keys(self): # Test case with three nodes of equal keys, but only need to find two
