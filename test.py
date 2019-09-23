#Python program to find LCA of node and node2 using a simple tree travesal in bottom to up fashion.
#Program assumes that the nodes are present in the tree
class Node:
    #Constructor for creating binary tree
    def __init__(current,key):
        current.key = key
        current.left = None
        current.right = None
    # Function that returns pointer of LCA of two nodes
def findLCA(root, node1, node2):

    if root is None:    #Base Case
        return None;

    if root.key == node1 or root.key == node2: # Node1/2 is LCA Case
        return root

    left_lca = findLCA (root.left, node1, node2) # Traverse Left and right subtrees, searching for node 1 and node 2
    right_lca = findLCA (root.right, node1, node2)

    if left_lca and right_lca: # if both functions return Non-Null, then current node is LCA
        return root

    return left_lca if left_lca is not None else right_lca # Otherwise check if left or right subtree is lCA
#Test Temporary Tree with nodes
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("LCA(4,5) = ",findLCA(root, 4, 5).key)
print("LCA(4,6) = ",findLCA(root, 4, 6).key)
print("LCA(3,4) = ",findLCA(root, 3, 4).key)
print("LCA(2,4) = ",findLCA(root, 2, 4).key)
