class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r
        
        while l <= r:
            k = (l + r) // 2
            
            total_hours = 0
            for p in piles:
                # 替代 math.ceil(p / k) 的整數公式
                total_hours += (p + k - 1) // k
            
            if total_hours <= h:
                ans = k
                r = k - 1
            else:
                l = k + 1
                
        return ans

