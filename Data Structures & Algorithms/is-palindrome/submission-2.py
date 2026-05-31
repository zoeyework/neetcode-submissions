class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_list = [c for c in s if c.isalnum()]
        isalnum_string = "".join(char_list)
        isalnum_string=isalnum_string.lower()
        print(isalnum_string)
        string_i=isalnum_string
        string_j=""
        j = len(isalnum_string)-1
        while j >=0:
            string_j += isalnum_string[j]
            j-=1
        print(string_i)
        print(string_j)
        return string_i ==string_j
        