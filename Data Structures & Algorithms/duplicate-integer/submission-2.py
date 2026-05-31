class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = []
        for x in nums:   
            if x in new_nums:
                print('Duplicated_Number')
                print(x)
                return True
            if x not in new_nums:
                new_nums.append(x)
                print(new_nums) # Time Complexity = O(n)
        else: 
            return False


                      
        