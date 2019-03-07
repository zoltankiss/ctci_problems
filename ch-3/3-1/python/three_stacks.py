class ThreeStacks:
    def __init__(self):
        self.data = []

    def push(self, stack, e):
        k = stack
        f = None
        while k < len(self.data):
            if self.data[k] is None:
                f = k
                break
            k = k + 3
        if f is None:
            for i in range(0, 3):
                if i == stack:
                    self.data.append(e)
                else:
                    self.data.append(None)
        else:
            self.data[f] = e

    def pop(self, num):
        f = num
        while f + 3 < len(self.data):
            if self.data[f] is None:
                break
            f = f + 3
        if self.data[f] is None:
            f = f - 3
        if f >= 0:
            val = self.data[f]
            self.data[f] = None
            return val
        raise Exception("nothing to pop")
