class MinStack():
    def __init__(self):
        self.stack = []
        self.minStack=[]

    def push(self, val: int) -> None:
        # 1. 正常的數字進 stack
        self.stack.append(val)
        
        # 2. 決定要不要更新最小值的筆記本 (min_stack)
        # 如果 min_stack 是空的，或者目前的 val 比筆記本最後一個還小
        # 就把 val 也放進 min_stack
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
