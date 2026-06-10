class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            # 如果中間值比右邊界大，代表最小值在右側
            if nums[mid] > nums[r]:
                l = mid + 1
            # 否則，最小值在左側（包含 mid 本身）
            else:
                r = mid
                
        # 當 l == r 時，就是最小值的位置
        return nums[l]