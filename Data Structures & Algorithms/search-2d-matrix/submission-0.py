class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        # m: 有幾列 (rows), n: 每列有幾個元素 (cols)
        m, n = len(matrix), len(matrix[0])
        
        # 這裡修正了：不能用 len()，直接相乘就是總數
        l, r = 0, (m * n) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            # 這裡修正了： row 是除以 n (寬度)
            row = mid // n
            col = mid % n
            
            # 取出矩陣中的數值來比較
            guess = matrix[row][col]
            
            if guess == target:
                return True
            
            # 根據數值大小移動邊界
            if guess < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return False
