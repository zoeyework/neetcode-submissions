class MinStack:
    def __init__(self):
        self.stack=[] # 創空 stack 
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val) 
        if self.min_stack:
            current_min=min(self.min_stack[-1],val)
            self.min_stack.append(current_min)
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
