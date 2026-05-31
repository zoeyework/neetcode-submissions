class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = []
        for x in nums:
            if x in new_nums:
                return True
            if x not in new_nums:
                new_nums.append(x)
        else: return False


                      
        