class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_length = 0
        start = 0  # The left boundary of our sliding window
        
        for i, char in enumerate(s):
            # If we've seen the character AND it's inside our current window
            if char in seen and seen[char] >= start:
                # Move the start to right after the previous occurrence
                start = seen[char] + 1
            
            # Update the last seen index of the character
            seen[char] = i
            # Calculate current window size: (current_index - start + 1)
            max_length = max(max_length, i - start + 1)
            
        return max_length
        