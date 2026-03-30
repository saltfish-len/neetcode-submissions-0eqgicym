class MinStack:

    def __init__(self):
        self.min = None
        self.stack = []
        self.mstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min is not None:
            self.min = min(self.min, val)
        else:
            self.min = val
        self.mstack.append(self.min)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.mstack.pop(-1)
        if len(self.mstack) > 0:
            self.min = self.mstack[-1]
        else:
            self.min = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
        
