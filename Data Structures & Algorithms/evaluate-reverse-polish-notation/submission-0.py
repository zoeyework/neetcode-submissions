class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        
        for token in tokens:
            if token in operators:
                # 碰到符號了！從 stack 抓出最後兩個數字
                # 注意：後出來的是左邊的數，先出來的是右邊的數
                num2 = stack.pop()
                num1 = stack.pop()
                
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                elif token == '/':
                    # 這是 Python 處理「向 0 取整」的小技巧
                    stack.append(int(num1 / num2))
            else:
                # 如果是數字，轉成整數後丟進 stack
                stack.append(int(token))
                
        # 最後 stack 裡只會剩下一個數字，就是答案！
        return stack[0]
            
        