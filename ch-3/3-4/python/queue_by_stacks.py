# implement a queue using two stacks
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, element):
        self.stack1.append(element)

    def pop(self):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        val = self.stack2.pop()
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return val
