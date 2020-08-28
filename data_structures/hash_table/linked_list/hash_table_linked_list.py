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

    def search(self, data):
        currNode = self.head
        while (currNode):
            if (currNode.value == data):
                print("Found {} in the linked list".format(data))
                return data
            currNode = currNode.next;
        print("{} does not exist in the linked list".format(data))

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