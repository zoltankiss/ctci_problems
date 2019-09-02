class Stack:
    def __init__(self, lst):
        self.lst = lst

    def push(self, e):
        self.lst.append(e)

    def pop(self):
        return self.lst.pop()

    def peek(self):
        return self.lst[-1]

    def isEmpty(self):
        return self.lst == []

class SortStack:
    def __init__(self):
        self.stck = Stack([])

    def sort(self, stack):
        while not stack.isEmpty():
            top = stack.pop()
            counter = 0
            if self.stck.isEmpty():
                self.stck.push(top)
            else:
                if self.stck.peek() > top:
                    self.stck.push(top)
                else:
                    while self.stck.peek() < top:
                        counter =+ 1
                        stack.push(self.stck.pop())
                    self.stck.push(top)
                    for _ in range(0, counter):
                        self.stck.push(stack.pop())
        return self.stck
