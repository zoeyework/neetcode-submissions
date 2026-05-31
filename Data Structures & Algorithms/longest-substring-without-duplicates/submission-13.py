class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head=0
        seen={}
        max_current_length=0
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]]>=head:
                head = seen[s[i]]+ 1
            current_length= i - head +1
            max_current_length=max(max_current_length,current_length)
            seen[s[i]]=i
        return max_current_length        