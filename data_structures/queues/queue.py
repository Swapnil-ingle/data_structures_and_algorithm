class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = -1
        self.tail = -1

    def enqueue(self, element):
        # Check whether queue is full
        if (self.head == self.tail and self.head != -1 and self.queue[self.head] != None):
            print("Cannot enqueue {} - Queue is full!".format(element))
            return
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = element
        if (self.tail == -1):
            self.tail = self.size - 1

    def dequeue(self):
        # Check whether the queue is empty
        if (self.head == -1):
            print("Cannot DeQueue - Queue is empty!")
            return
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = None

    def print(self):
        print("########## Printing Queue ###########")
        print(" - ".join(map(str, self.queue)))
        print("Head is at: {} ".format(self.head))
        print("Tail is at: {}".format(self.tail))


# Driver code
queue = Queue(5)
queue.dequeue()
queue.enqueue(5)
queue.print()
queue.dequeue()
queue.print()
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.dequeue()
queue.dequeue()
queue.enqueue(9)
queue.print()