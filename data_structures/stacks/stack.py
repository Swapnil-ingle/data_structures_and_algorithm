class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.head = 0

    def push(self, element):
        # Check if stack is full
        if (self.head >= self.size):
            print("Cannot add element - stack is full!")
        else:
            self.stack[self.head] = element
            self.head = self.head + 1
            print("Pushed element!")

    def pop(self):
        # Check if stack is empty
        if (self.head == 0):
            print("Cannot pop element - stack is empty!")
        else:
            self.head = self.head - 1
            del self.stack[self.head]
            print("Pop'd element!")

    def print(self):
        for item in self.stack:
            print(item)
        print("Head is at - ", end="")
        print(self.head)

# Driver code
stack = Stack(5)
stack.print();
stack.pop();
stack.push(1);
stack.push(2);
stack.push(3);
stack.push(4);
stack.push(5);
stack.push(6);
stack.pop();
stack.push(7);