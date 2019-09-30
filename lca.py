#Python program to find LCA of node and node2 using a simple tree travesal in bottom to up fashion.

# Function that returns pointer of LCA of two nodes
# found1 is set as true by this function if node1 is found
# found2 is set as true by this function if node2 is found
def findLCAUtil(root, node1, node2, found):
    if root is None:    #Base Case
        return None

    if root.value == node1: # Node1 is LCA Case
        found[0] = True # Found node1 = True
        return root
    if root.value == node2: # Node1 is LCA Case
        found[1] = True # Found node2 = True
        return root

    left_lca = findLCAUtil(root.left, node1, node2, found) # Traverse Left and right subtrees, searching for node 1 and node 2
    right_lca = findLCAUtil(root.right, node1, node2, found)

    if left_lca and right_lca: # if both functions return Non-Null, then current node is LCA
        return root

    return left_lca if left_lca is not None else right_lca # Otherwise check if left or right subtree is lCA
    
#Function that returns true/false if the node is present
def find(root, k):

    # Base Case
    if root is None:
        return False

    # If key is present at root, or if left subtree or right
    # subtree , return true
    if (root.value == k or find(root.left, k) or find(root.right, k)):
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
