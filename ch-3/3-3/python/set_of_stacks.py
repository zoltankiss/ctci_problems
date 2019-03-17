class SetOfStacks:
    def __init__(self, stack_max_len):
        self.stack_max_len = stack_max_len
        self.stacks = [[]]
        self.current_pos = 0

    def push(self, element):
        if len(self.stacks[len(self.stacks) - 1]) < self.stack_max_len:
            self.stacks[len(self.stacks) - 1].append(element)
        else:
            self.stacks.append([element])

    def pop(self):
        if not self.stacks[len(self.stacks) - 1]:
            self.stacks = self.stacks[0:-1]
        last_element = self.stacks[len(self.stacks) - 1][-1]
        self.stacks[len(self.stacks) - 1] = self.stacks[len(self.stacks) - 1][0:-1]
        return last_element
