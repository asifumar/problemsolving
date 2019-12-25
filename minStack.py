class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        
    def push(self, x: int) -> None:
        self.l.append(x)       

    def pop(self) -> None:
        self.l.pop()
        

    def top(self) -> int:
        return self.l[-1]
        

    def getMin(self) -> int:
        return min(self.l)

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)

print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
print(minStack.l)