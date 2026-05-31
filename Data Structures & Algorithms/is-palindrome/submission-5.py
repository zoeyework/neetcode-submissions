class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string=s.replace(" ","")
        print(cleaned_string)
        lower_string=cleaned_string.lower()
        cleaned_text = "".join(char for char in lower_string if char.isalnum())
        print(cleaned_text)
        return cleaned_text == cleaned_text[::-1]