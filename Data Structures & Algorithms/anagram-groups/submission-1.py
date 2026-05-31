class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res ={}
        for s in range(len(strs)):
            print(strs[s])
            count={}
            for character in strs[s]:
                count[character] = 1+count.get(character,0) 
            sorted_count=tuple(sorted(count.items()))
            if sorted_count not in res:
                res[sorted_count] = []
            res[sorted_count].append(strs[s])
        return list(res.values()) 
'''
Time Complexity = O(n*slogs) 
n = 外層 每一陣列元素 
s = 內層 每一個元素需要遍歷字母
logs = 字母排序需要logs 時間
'''