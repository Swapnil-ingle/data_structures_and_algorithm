from linked_list import hash_table_linked_list
#
# --- Hash Function ---
# A Hash Function takes the key (int/float/string) and converts
# it to an index. Which is then used to put that key-value pair.
#
# --- A good hash function should ---
# Distribute the keys uniformly across the hash-table and results
# in minimum collision.#
#
# For Positive Integer --> Modular hashing
# In modular hashing, we take an array of prime size 'M' and, for any
# positive integer k, we do M % k. This will uniformly distribute the
# positive integers.
# Q: Why prime sized array? (Read: https://cs.stackexchange.com/questions/11029/why-is-it-best-to-use-a-prime-number-as-a-mod-in-a-hashing-function)
#
# #

class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self):
        self.size = 13
        self.hashTable = [self.size]

    def hash(self, key):
        return self.size % key

    def put(self, key, value):
        # Hash the incoming key and put in hashTable
        keyLink = self.hashTable[self.hash(key)]
        if (keyLink is None):
            keyLink = LinkedList()
        alreadyPresent = keyLink.search(Node(key, value))
        if (alreadyPresent != None):
            alreadyPresent = Node(key, value)
            return
        keyLink.insert(Node(key, value))

    def print(self):
        for i in self.hashTable:
            if (i != None):
                i.print
                continue
            print(i)


# Driver code
hashTable = HashTable()
hashTable.print()
hashTable.put(1, 'abc')
hashTable.print()
