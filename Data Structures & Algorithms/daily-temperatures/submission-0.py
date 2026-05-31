class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1. 初始化結果陣列，預設為 0 (如果找不到更高的就是 0)
        res = [0] * len(temperatures)
        
        # 2. 建立 stack，用來儲存「還沒找到更高溫度的索引 (index)」
        stack = [] 
        
        # 3. 正向遍歷一遍
        for i, t in enumerate(temperatures):
            # 當 stack 不為空，且當前溫度比 stack 頂端的溫度還要高時
            while stack and t > temperatures[stack[-1]]:
                # 彈出舊的 index
                prev_index = stack.pop()
                # 計算天數差：當前 index - 舊的 index
                res[prev_index] = i - prev_index
            
            # 把當前的 index 放進去等待
            stack.append(i)
            
        return res