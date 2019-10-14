
# Cannot traverse paths from root to the two nodes and look for the last equal element, as there is not necessarily a single path to a given node from the root and a node can have multiple parents.
class Node:
    def __init__(self,key):
        self.key = key
        self.pred = []  # list of predecessor, before
        self.succ = []  # list of successor, after

def daglca(root, node1,node2):
    if root is None: # empty tree
        return None
    if root.key == node1.key or root.key == node2.key: # root is one of the nodes
        return root.key
    if node1.key == node2.key: # nodes have same keys
        return node1.key

    lca = [] # list of common ancestors, use max to get lowest.
#range() : generates a sequence of numbers over time.
#len() : returns the number of items in an object.

    for i in range(len(node1.pred)): # length of number of pred nodes before node
        for j in range(len(node2.pred)):
            if(node1.pred[i].key == node2.pred[j].key):
                lca.append(node1.pred[i].key)

    if(lca == [] ) :
        if(node1.key > node2.key):
            lca.append(daglca(root,node1.pred[0], node2)) #set depth to 0 and start backtracking
        else:
            lca.append(daglca(root, n1, n2.pred[0]))
    return max(lca)
