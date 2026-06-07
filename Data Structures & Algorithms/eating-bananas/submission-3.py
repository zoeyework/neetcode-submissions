class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1. 找出最大值作為右邊界
        max_p = 0
        for pile in piles:
            max_p = max(max_p, pile)
            
        # 設定二分搜尋的範圍
        left = 1
        right = max_p
        k_ans = max_p # 用一個變數來記錄目前最安全、最好的答案
        
        # 2. 當左邊界還沒超過右邊界時，持續折半尋找
        while left <= right:
            # 每次取範圍的中間值作為測試速度，這就是你原本想做的折半 (int(k/2))
            mid = (left + right) // 2 
            
            # 💡 關鍵點：每次換新速度測試，總小時數一定要歸零！
            sum_value = 0 
            
            # 計算以速度 mid 吃完需要多少小時
            for p in piles:
                # 使用無條件進位，確保餘數也有算到小時
                value = (p + mid - 1) // mid
                sum_value += value
            
            print(f'嘗試速度 mid: {mid}, 總花費小時 total_hour: {sum_value}, 目標 h: {h}')
            
            # 3. 根據花費時間，調整搜尋範圍
            if sum_value <= h:
                # 能夠在 h 小時內吃完，代表這個速度可行！
                k_ans = mid       # 先記錄下來這個成功過關的速度
                right = mid - 1   # 既然成功了，那我們試試看更慢（更小）的速度行不行
            else:
                # sum_value > h，代表吃太慢了，時間不夠用
                left = mid + 1    # 我們必須提高速度，把下限調高
                
        return k_ans