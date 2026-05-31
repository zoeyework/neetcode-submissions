class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        postfix=[]
        value = 1
        for i in range(len(nums)):
            prefix.append(value)
            value=value*nums[i]
        value = 1    
        for i in range(len(nums) - 1, -1, -1):
            postfix.append(value)
            value=value*nums[i]
        postfix.reverse()
        print(prefix)
        print(postfix)
        res = [prefix[i] * postfix[i] for i in range(len(nums))]
        return res
            



            
        