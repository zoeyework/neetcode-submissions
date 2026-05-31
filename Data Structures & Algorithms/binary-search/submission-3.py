class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1 
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                res= mid
                break
            else: 
                if nums[mid] < target:
                    l =mid+1
                else: 
                    r = mid-1
        return res

#nums=[-1,0,2,4,6,8]
#target=3


        