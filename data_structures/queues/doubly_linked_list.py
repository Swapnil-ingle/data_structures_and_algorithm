class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def length(self):
        currNode = self.head
        length = 0
        while (currNode):
            length = length + 1
            currNode = currNode.next
        return length

    def print(self):
        print("######### Printing Doubly LinkedList #########")
        currNode = self.head
        list = []
        while (currNode):
            list.append("[{}]".format(currNode.value))
            currNode = currNode.next
        print(" <-> ".join(map(str, list)))

    def revPrint(self):
        print("######### Printing Reverse Doubly LinkedList #########")
        currNode = self.tail
        list = []
        while (currNode):
            list.append("[{}]".format(currNode.value))
            currNode = currNode.prev
        print(" <-> ".join(map(str, list)))

    def search(self, data):
        currNode = self.head
        while (currNode):
            if (currNode.value == data):
                print("Found {} in the doubly linked list".format(data))
                return data
            currNode = currNode.next
        print("{} does not exist in the doubly linked list".format(data))

    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
            newNode.prev = current
        else:
            self.head = newNode
        self.tail = newNode

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
            currNode.prev = prevNode
        else:
            self.head = self.head.next

        if (currNode.next is None):
            self.tail = self.tail.prev
        # Deleting currNone
        currNode = None

    def reverse(self):
        currNode = self.head
        lastNode = self.tail
        for i in range(0, self.length()//2):
            currNode.value, lastNode.value = lastNode.value, currNode.value
            currNode = currNode.next
            lastNode = lastNode.prev

    def sortAsc(self):
        self._sort(1)

    def sortDesc(self):
        self._sort(-1)

    def _sort(self, order):
        currNode = self.head
        sortedList = []
        while (currNode):
            sortedListLenght = len(sortedList)
            currVal = currNode.value
            # Compare with the element at last index
            if (sortedListLenght >= 1):
                biggestVal = sortedList[sortedListLenght - 1]
                sortedList.append(currVal)
                if (biggestVal > currVal):
                    sortedList[sortedListLenght], sortedList[sortedListLenght -
                                                             1] = sortedList[sortedListLenght - 1], sortedList[sortedListLenght]
            else:
                sortedList.append(currVal)
            currNode = currNode.next

        currNode = self.head
        if (order == 1):
            for i in sortedList:
                currNode.value = i
                currNode = currNode.next
        else:
            for i in sortedList[::-1]:
                currNode.value = i
                currNode = currNode.next


# Driver code
dll = DoublyLinkedList()
dll.insert(2)
dll.insert(3)
dll.insert(4)
dll.print()
dll.revPrint()
dll.delete(3)
dll.delete(4)
dll.delete(2)
dll.print()
dll.revPrint()
dll.insert(7)
dll.insert(2)
dll.insert(4)
dll.insert(5)
dll.insert(12)
dll.print()
dll.sortAsc()
dll.print()
dll.sortDesc()
dll.print()
dll.reverse()
dll.print()