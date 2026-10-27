class MinStack:

    def __init__(self):
        self.val = None
        self.arr = []
        self.least = None
        

    def push(self, val: int) -> None:
        if self.least == None:
            self.least = val
        elif self.least > val:
            self.least = val
        self.arr.append((val, self.least))

    def pop(self) -> None:
        self.arr.pop()
        self.least = self.arr[-1][1]

    def top(self) -> int:
        return self.arr[-1][0]
        

    def getMin(self) -> int:
        return self.least
        
