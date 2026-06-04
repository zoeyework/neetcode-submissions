class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1. 定義速度的搜尋範圍
        left = 1
        right = max(piles)
        ans = right  # 先預設最大值為答案
        
        # 2. 開始二分搜尋
        while left <= right:
            mid = (left + right) // 2  # 當前嘗試的速度
            
            # 計算用速度 mid 吃完所有香蕉需要多少小時
            total_hours = 0
            for p in piles:
                # (p + mid - 1) // mid 是整數無條件進位的寫法
                total_hours += (p + mid - 1) // mid 
            
            # 3. 判斷這個速度可不可行
            if total_hours <= h:
                ans = mid          # 這個速度可以，先記錄下來
                right = mid - 1    # 試試看有沒有更慢（更小）的速度
            else:
                left = mid + 1     # 太慢了，必須提高速度
                
        return ans