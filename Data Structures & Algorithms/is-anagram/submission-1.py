#s='racecar', t='carrace'
#Time Complexity = O(nlogn)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        CountS=[]
        CountT=[]

        for i in range(len(s)):
            CountS.append(s[i])
            CountT.append(t[i])
        CountS.sort()
        CountT.sort()
        return CountS == CountT