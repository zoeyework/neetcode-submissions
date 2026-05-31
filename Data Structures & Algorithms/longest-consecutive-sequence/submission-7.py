class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        print(nums_set)
        max_len_seq=0
        len_seq=0
        for n in nums:
            if n-1 not in nums_set:
                len_seq=0
                while n+len_seq in nums_set:
                    len_seq +=1
                    max_len_seq=max(max_len_seq,len_seq)
        return max_len_seq
                
        