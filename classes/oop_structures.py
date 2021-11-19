class DataCollection:
    def __init__(self):
        self.elements = []

    def add(self, item):
        self.item = item
        self.elements.append(self.item)

    def pop(self):
        return None

    def size(self):
        return len(self.elements)

class Stack(DataCollection):
    def pop(self):
        return self.elements.pop()

class Queue(DataCollection):
    def pop(self):
        return self.elements.pop(0)


stack = Stack()
stack.add(1)
stack.add(2)
stack.add(3)
print(stack.elements)
print(stack.pop())
print(stack.pop())
print(stack.pop())

queue = Queue()
queue.add('a')
queue.add('b')
queue.add('c')
print(queue.elements)
print(queue.pop())
print(queue.pop())
print(queue.pop())
