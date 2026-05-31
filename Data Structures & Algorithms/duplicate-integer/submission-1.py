class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()  # 使用集合，查詢速度極快
        for x in nums:
            if x in seen:
                return True   # 只要發現看過的，直接回傳 True
            seen.add(x)       # 沒看過，就加進去
            
        return False          # 整個迴圈跑完都沒 return，代表沒重複
        