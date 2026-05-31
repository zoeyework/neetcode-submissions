class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        count={}
        for i in range(len(nums)):
            count[nums[i]] = 1+count.get(nums[i],0)
        print(count)
        sorted_count={k:v for k,v in sorted(count.items(),key=lambda item:item[0])}
        print(sorted_count)
        current_consecutive_length=1
        max_consecutive_length=1
        key_list =list(sorted_count.keys())
        for i in range(len(key_list)-1):
            if key_list[i+1] == key_list[i] +1:
                current_consecutive_length +=1
            else: 
                max_consecutive_length = max(max_consecutive_length,current_consecutive_length)
                current_consecutive_length=1
        return max(max_consecutive_length,current_consecutive_length)



        
            

            
        