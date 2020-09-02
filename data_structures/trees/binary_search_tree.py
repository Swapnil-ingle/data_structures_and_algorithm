class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    def getHeight(self):
        if self.root is None:
            return 0

        return self._getHeight(self.root)

    def _getHeight(self, curr_node):
        if (curr_node is None):
            return 0
        lHeight = self._getHeight(curr_node.left_child)
        rHeight = self._getHeight(curr_node.right_child)

        if (lHeight > rHeight):
            return lHeight + 1
        else:
            return rHeight + 1

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, curr_node):
        if value < curr_node.value:
            if curr_node.left_child is None:
                curr_node.left_child = Node(value)
                curr_node.left_child.parent = curr_node
            else:
                self._insert(value, curr_node.left_child)
        elif value > curr_node.value:
            if (curr_node.right_child is None):
                curr_node.right_child = Node(value)
                curr_node.right_child.parent = curr_node
            else:
                self._insert(value, curr_node.right_child)
        else:
            print(value)
            print("This value is already present")

    def printTree(self):
        if self.root != None:
            self._printTree(self.root)
        print("")

    def _printTree(self, curr_node):
        if (curr_node != None):
            self._printTree(curr_node.left_child)
            print(curr_node.value, end=' ')
            self._printTree(curr_node.right_child)

    def search(self, value):
        if (self.root != None and self.root.value == value):
            return True
        elif (self.root.value > value):
            return self._search(value, self.root.left_child)
        else:
            return self._search(value, self.root.right_child)

    def _search(self, value, curr_node):
        if (curr_node is None):
            return False
        if (curr_node.value == value):
            return True
        elif (curr_node.value > value):
            return self._search(value, curr_node.left_child)
        else:
            return self._search(value, curr_node.right_child)

    def min(self):
        if (self.root is None):
            return None
        if (self.root.left_child is None):
            return root.value
        else:
            return self._min(self.root.left_child)

    def _min(self, curr_node):
        if (curr_node is None):
            return curr_node.parent.value
        if (curr_node.left_child is None):
            return curr_node.value
        return self._min(curr_node.left_child)

    def max(self):
        if (self.root is None):
            return False
        if (self.root.right_child is None):
            return self.root.value
        return self._max(self.root.right_child)

    def _max(self, curr_node):
        if (curr_node is None):
            return False
        if (curr_node.right_child is None):
            return curr_node.value
        return self._max(curr_node.right_child)

    def getNodeFromValue(self, value):
        if (self.root != None and self.root.value == value):
            return self.root
        elif (self.root.value > value):
            return self._getNodeFromValue(value, self.root.left_child)
        else:
            return self._getNodeFromValue(value, self.root.right_child)

    def _getNodeFromValue(self, value, curr_node):
        if (curr_node is None):
            return None
        if (curr_node.value == value):
            return curr_node
        if (curr_node.value > value):
            return self._getNodeFromValue(value, curr_node.left_child)
        else:
            return self._getNodeFromValue(value, curr_node.right_child)

    def successorOf(self, curr_node):
        # Case 1: If right subtree is non-empty --> Succ is min(right_subtree)
        if (curr_node.right_child != None):
            return self._min(curr_node.right_child)
        # Case 2: If right subtree is empty:
        # Go to parent until current_node was NOT in the right of parent
        while (True):
            temp = curr_node.parent
            if (temp is None):
                print("This key has no succesor!!")
                break
            if (temp.right_child != None and curr_node.value == temp.right_child.value):
                curr_node = temp
                continue
            else:
                return temp.value

    def predecessorOf(self, curr_node):
        # Case 1: If left subtree is non-empty --> Predecessor is min(left_subtree)
        if (curr_node.left_child != None):
            return self._min(curr_node.left_child)

        # Case 2: If left subtree is empty:
        # Go to parent until current_node was NOT in the left of parent
        while (True):
            temp = curr_node.parent
            if (temp is None):
                print("This key has no succesor!!")
                break
            if (temp.left_child != None and curr_node.value == temp.left_child.value):
                curr_node = temp
                continue
            else:
                return temp.value

    def deleteValue(self, value):
        self.delete(self.getNodeFromValue(value))

    def delete(self, curr_node):
        if (curr_node is None):
            print("Either node does not exists or is empty.")
            return False

        def _deleteNodeWithNoChildren(curr_node):
            parent = curr_node.parent
            if (_isDeletingNodeALeftChild(parent, curr_node)):
                parent.left_child = None
            else:
                parent.right_child = None
            curr_node = None

        def _deleteNodeWithOneChild(curr_node, non_null_child):
            parent = curr_node.parent
            non_null_child.parent = parent
            if (_isDeletingNodeALeftChild(parent, curr_node)):
                parent.left_child = None
                parent.left_child = non_null_child
            else:
                parent.right_child = None
                parent.right_child = non_null_child
            parent = None
            curr_node = None

        def _deleteNodeWithTwoChildren(curr_node):
            succ = self.getNodeFromValue(self.successorOf(curr_node))
            self.delete(succ)
            curr_node.value = succ.value

        def _isDeletingNodeALeftChild(parent, curr_node):
            if (parent.left_child != None and parent.left_child.value == curr_node.value):
                return True
            else:
                return False

        if (curr_node.parent is None):
            # Deleting root node
            _deleteNodeWithTwoChildren(curr_node)
            return

        non_null_child = curr_node.left_child if curr_node.left_child != None else curr_node.right_child
        # Case 0: If the curr_node has no children
        if (non_null_child is None):
            _deleteNodeWithNoChildren(curr_node)
            return

        # Case 1: If the curr_node has one child
        if (curr_node.left_child is None or curr_node.right_child is None):
            _deleteNodeWithOneChild(curr_node, non_null_child)
            return

        # Case 2: If the curr_node has two children --> Find succesor replace and delete
        if (curr_node.left_child != None and curr_node.right_child != None):
            _deleteNodeWithTwoChildren(curr_node)


# Driver Code:
tree = BST()
# Inserting in the Binary Search Tree
print("Insertion Operation...")
tree.insert(5)
tree.insert(2)
tree.insert(10)
tree.insert(1)
tree.insert(3)
tree.insert(7)
tree.insert(8)
# Printing the Tree
print("Printing the Tree: ", end="")
tree.printTree()
# Searching Operation
print("Searching Operation - Does 2 exists? ", end="")
print(tree.search(2))
# Minimum node
print("Minimum node in the tree is: ", end="")
print(tree.min())
# Maximum node
print("Maximum node in the tree is: ", end="")
print(tree.max())
# Successor Of a Node
print("Successor of 3 is: ", end="")
print(tree.successorOf(tree.getNodeFromValue(3)))
# Predecessor Of a Node
print("Predecessor of 7 is: ", end="")
print(tree.predecessorOf(tree.getNodeFromValue(7)))
# Deletion of a node
print("Deleting 5 from the tree: ", end="")
tree.deleteValue(5)
print("Tree after deletion is: ", end="")
tree.printTree()
# Printing height of tree
print("Printing height of tree: ", end="")
print(tree.getHeight())
