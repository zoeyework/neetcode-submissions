class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #target = 7
        #array nums=[3,4,5,6]
       for i in range(len(nums)):
           y = target - nums[i]
           print(y)
           for j in range(i+1,len(nums)):
                if nums[j] == y and i != j:
                    return [i,j]

        