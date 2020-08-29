
# --- Hash Function ---
# A Hash Function takes the key (int/float/string) and converts
# it to an index. Which is then used to put that key-value pair.
#
# --- A good hash function should ---
# Distribute the keys uniformly across the hash-table and results
# in minimum collision.#
#
# --- Different Hashing Functions ---
# * For Positive Integer --> Modular hashing
# In modular hashing, we take an array of prime size 'M' and, for any
# positive integer k, we do k % M. This will uniformly distribute the
# positive integers.
# Q: Why prime sized array?
# A: (Read: https://cs.stackexchange.com/questions/11029/why-is-it-best-to-use-a-prime-number-as-a-mod-in-a-hashing-function)
#
# * For Floating Point Numbers --> Do NOT Hash!
# As floating point formats are often platform dependent and equality checking
# (given all the point precision) is not reliable.
# "Hashing floating-point numbers is as dangerous as directly checking for their equality
# using the == operator. Even tiny differences in their values may throw them into different
# buckets of an associated hash table."
# Check (https://stackoverflow.com/questions/7403210/hashing-floating-point-values)
# (https://diego.assencio.com/?index=67e5393c40a627818513f9bcacd6a70d)
#
# * For String --> Polynomial rolling hash function
# A rolling hash (also known as recursive hashing or rolling checksum) is a hash function where
# the input is hashed in a window that moves through the input.
#
# Ex: The three letter word ace could turn into a number by calculating:
# key = (1 _ 26^2 + 3 _ 26^1 + 5 * 26^0) Mod M
# Read: (https://advancedweb.dev/polynomial-rolling-hash)
#
# --- Collision Resolution ---
# A chaining LinkedList is used for collision resolution in this implementation.#

# Inner LinkedList
# TODO --> Move this to other file
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
        currNode = self.head
        list = []
        while (currNode):
            list.append("[{}]".format(currNode.value.__str__()))
            currNode = currNode.next
        return (" -> ".join(map(str, list)))

    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def search(self, key):
        currNode = self.head
        while (currNode):
            if (currNode.value.key == key):
                # print("Found {} in the linked list".format(data))
                return currNode
            currNode = currNode.next
        # print("{} does not exist in the linked list".format(data))

    def delete(self, element):
        currNode = self.head
        prevNode = None
        while (currNode != None and currNode.value != element):
            prevNode = currNode
            currNode = currNode.next

        if (currNode is None):
            # print("Cannot delete - '{}' not found!".format(element))
            return

        if (prevNode != None):
            prevNode.next = currNode.next
        else:
            self.head = self.head.next
        currNode = None


class KeyVal:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def __str__(self):
        return ("[{},{}]".format(self.key, self.value))


class HashTable:
    def __init__(self):
        self.size = 13
        self.hashTable = [None] * self.size

    def hash(self, key):
        if (isinstance(key, int)):
            return key % self.size
        elif (isinstance(key, float)):
            raise TypeError("Cannot hash floats!")
        elif (isinstance(key, str)):
            return self._hashString(key, self.size)

    def _hashString(self, key, arraySize):
        base = 13
        hash = 0
        charIdx = 0
        for i in key:
            hash = (hash * base + (ord(i.lower()) - 96)) % arraySize
        return hash

    def put(self, key, value):
        # Hash the incoming key and put in hashTable
        hashedKey = self.hash(key)
        bucket = self.hashTable[hashedKey]
        currKeyVal = KeyVal(key, value)
        if (bucket is None):
            bucket = LinkedList()
        alreadyPresent = bucket.search(currKeyVal.key)
        if (alreadyPresent != None):
            alreadyPresent.value.value = currKeyVal.value
            return
        bucket.insert(currKeyVal)
        if (self.hashTable[hashedKey] == None):
            self.hashTable[hashedKey] = bucket

    def get(self, key):
        for bucket in self.hashTable:
            if (bucket is None):
                continue
            found = bucket.search(key)
            if (found):
                return found.value.value
        return None

    def print(self):
        print("###### Printing Hash Table ######")
        printable = []
        for i in self.hashTable:
            if (i != None):
                printable.append(i.print())
                continue
            printable.append(i)
        print(", ".join(map(str, printable)))


# Driver code
hashTable = HashTable()
hashTable.print()
hashTable.put(1, 'Sam')
hashTable.put(1, 'Max')
hashTable.put(5, 'Ali')
hashTable.put(23, 'Chandler')
hashTable.print()
print(hashTable.get(5))
print(hashTable.get(6))
hashTable.put("Sam", 123)
hashTable.put("Samuel", 456)
hashTable.put("Max", 1234)
hashTable.print()
print(hashTable.get("Max"))