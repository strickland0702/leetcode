class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minstack or x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self) -> None:
        pop_number = self.stack.pop()
        if self.minstack and pop_number == self.minstack[-1]:
            self.minstack.pop()                           

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.minstack[-1] if self.minstack else None

# keep a stack and a minstack, use space to trade-off time. 

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()