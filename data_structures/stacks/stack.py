class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.head = -1

    def push(self, element):
        # Check if stack is full
        if (self.head >= self.size - 1):
            print("Cannot add element - stack is full!")
        else:
            self.head = self.head + 1
            self.stack[self.head] = element
            print("Pushed element!")

    def pop(self):
        # Check if stack is empty
        if (self.head == -1):
            print("Cannot pop element - stack is empty!")
        else:
            self.stack[self.head] = None
            self.head = self.head - 1
            print("Pop'd element!")

    def print(self):
        print("######### Printing Stack #########")
        stack = " - ".join(map(str, self.stack))
        print("(bottom) {} (top)".format(stack))


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