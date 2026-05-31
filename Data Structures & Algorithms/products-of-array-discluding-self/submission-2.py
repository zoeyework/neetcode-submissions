class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        prefix=[]
        left_value =1
        for i in range(len(nums)):
            res[i] = left_value
            left_value=nums[i]*left_value
            print(res[i])
        right_value =1 
        for i in range(len(nums)-1,-1,-1):
            print(f'i:{i}')
            res[i] = res[i]*right_value
            right_value = nums[i]*right_value
            print(res[i])
        return res
            
                         