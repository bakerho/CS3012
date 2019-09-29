#Python program to find LCA of node and node2 using a simple tree travesal in bottom to up fashion.
#Program assumes that the nodes are present in the tree
class Node:
    #Constructor for creating binary tree
    def __init__(current,key):
        current.key = key
        current.left = None
        current.right = None
    # Function that returns pointer of LCA of two nodes
    # found1 is set as true by this function if node1 is found
    # found2 is set as true by this function if node2 is found
def findLCAUtil(root, node1, node2, found):

    if root is None:    #Base Case
        return None

    if root.key == node1: # Node1 is LCA Case
        found[0] = True # Found node1 = True
        return root
    if root.key == node2: # Node1 is LCA Case
        found[1] = True # Found node2 = True
        return root

    left_lca = findLCAUtil(root.left, node1, node2, found) # Traverse Left and right subtrees, searching for node 1 and node 2
    right_lca = findLCAUtil(root.right, node1, node2, found)

    if left_lca and right_lca: # if both functions return Non-Null, then current node is LCA
        return root

    return left_lca if left_lca is not None else right_lca # Otherwise check if left or right subtree is lCA

def find(root, k):

    # Base Case
    if root is None:
        return False

    # If key is present at root, or if left subtree or right
    # subtree , return true
    if (root.key == k or find(root.left, k) or find(root.right, k)):
        return True

    # Else return false
    return False

# This function returns LCA of n1 and n2 onlue if both
# n1 and n2 are present in tree, otherwise returns None
def findLCA(root, node1, node2):

    # Initialize n1 and n2 as not visited
    found = [False, False]

    # Find lac of n1 and n2 using the technique discussed above
    lca = findLCAUtil(root, node1, node2, found)

    # Returns LCA only if both n1 and n2 are present in tree
    if (found[0] and found[1] or found[0] and find(lca, node2) or found[1] and
        find(lca, node1)):
        return lca

    # Else return None
    return None
#Test Temporary Tree with nodes

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

lca = findLCA(root, 4, 5)

if lca is not None:
    print ("LCA(4, 5) =", lca.key)
else :
    print ("Keys are not present")

lca = findLCA(root, 4, 10)
if lca is not None:
    print ("LCA(4,10) = ", lca.key)
else:
    print ("Keys are not present")
