from dag import daglca, Node

class TestDag:
    def test_basic(self): #Test for basic case, nodes present in graph
        root = Node(1)
        node1 = Node(2)
        node2= Node(3)
        node3 = Node (4)
        node4 = Node (5)
        node5 = Node (6)
        root.succ = [node1,node2,node3,node4]
        node1.succ = [node3]
        node1.pred = [root]
        node2.succ = [node3,node4]
        node2.pred = [root]
        node3.succ = [node4]
        node3.pred = [node1,node2,root]
        node4.pred = [node2,node3,root]
        node5.pred = [node3]

        lca = daglca (root, node3,node4)

        assert lca is 3, "test_basic failed"

    def test_root_node(self): # Test case where root is a node of interest for lca
        root = Node(1)
        node1 = Node(2)
        node2 = Node(3)
        root.succ = [node1,node2]

        lca = daglca(root, node1,node1)

        assert lca is 2

        lca = daglca(root,node2,root)

        assert lca is 1

        lca = daglca(root, node1, root)

        assert lca is 1, "test_root_node failed"

    def test_null(self): # Test case with empty graph
        root = None

        lca = daglca(root,1,2)

        assert lca is None,  "test_null failed"

    def test_lowest_node (self): # Test case with one of the lowest nodes in graph
        root = Node(1)
        node1 = Node(2)
        node2= Node(3)
        node3 = Node (4)
        node4 = Node (5)
        node5 = Node (6)
        root.succ = [node1,node2,node3,node4]
        node1.succ = [node3]
        node1.pred = [root]
        node2.succ = [node3,node4]
        node2.pred = [root]
        node3.succ = [node4]
        node3.pred = [node1,node2,root]
        node4.pred = [node2,node3,root]
        node5.pred = [node3]

        lca = daglca (root, node5,node1)

        assert lca is 1, "test_lowest_node failed"
