from dag import daglca, Node

class TestDag:
    def test_basic(self):
        node0 = Node(1)
        node1 = Node(2)
        node2= Node(3)
        node3 = Node (4)
        node4 = Node (5)
        node5 = Node (6)
        node0.succ = [node1,node2,node3,node4]
        node1.succ = [node3]
        node1.pred = [node0]
        node2.succ = [node3,node4]
        node2.pred = [node0]
        node3.succ = [node4]
        node3.pred = [node1,node2,node0]
        node4.pred = [node2,node3,node0]
        node5.pred = [node3]

        lca = daglca (node0, node3,node4)

        assert lca is 3

    def test_root_node(self):
        root = Node(1)
        node1 = Node(2)
        node2 = Node(3)
        root.succ = [node1,node2]

        lca = daglca(root, node1,node1)

        assert lca is 2

        lca = daglca(root,node2,root)

        assert lca is 1

        lca = daglca(root, node1, root)

        assert lca is 1

    def test_null(self):
        root = None

        lca = daglca(root,1,2)

        assert lca is None
