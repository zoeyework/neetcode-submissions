class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False
        
        s1_counts = Counter(s1)
        window_counts = Counter()

        for i in range(n2):
            # 1. Add the current character to the window
            window_counts[s2[i]] += 1
            
            # 2. If the window is too big, remove the leftmost character
            if i >= n1:
                left_char = s2[i - n1]
                if window_counts[left_char] == 1:
                    del window_counts[left_char]
                else:
                    window_counts[left_char] -= 1
            
            # 3. Compare the window to our target
            if s1_counts == window_counts:
                return True
                
        return False      