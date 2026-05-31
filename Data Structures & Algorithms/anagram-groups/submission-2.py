class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      anagrams={}
      for str in strs:
         sorted_string=sorted(str)
         print(sorted_string)
         sorted_key="".join(sorted_string)
         if sorted_key not in anagrams:
            anagrams[sorted_key] = []
         anagrams[sorted_key].append(str)
      return list(anagrams.values())
            