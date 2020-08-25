class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        currNode = self.head
        length = 0
        while (currNode):
            length = length + 1
            currNode = currNode.next
        return length

    def print(self):
        print("######### Printing LinkedList #########")
        currNode = self.head
        list = []
        while (currNode):
            list.append("[{}]".format(currNode.value))
            currNode = currNode.next
        print(" -> ".join(map(str, list)))

    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def insertAt(self, data, pos):
        # TODO: Finish this implementation
        currNode = self.head
        currPos = 0
        while (currNode and currPos < pos):
            currNode = currNode.next
            currPos += 1

    def delete(self, element):
        currNode = self.head
        prevNode = None
        while (currNode != None and currNode.value != element):
            prevNode = currNode
            currNode = currNode.next

        if (currNode is None):
            print("Cannot delete - '{}' not found!".format(element))
            return

        if (prevNode != None):
            prevNode.next = currNode.next
        else:
            self.head = self.head.next
        currNode = None


# Driver code
ll = LinkedList()
# print(ll.lenght())
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.print()
ll.delete(2)
ll.delete(4)
ll.delete(3)
ll.print()
