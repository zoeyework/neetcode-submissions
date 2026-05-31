class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seem = {}
        for num in nums:
         if num in seem:
            seem[num] += 1
         else:
            seem[num] =1 
        print(seem)
        sorted_items = sorted(seem.items(), key=lambda x: x[1], reverse=True)
        
        # 3. 取出前 K 個數字
        res = []
        for i in range(k):
            res.append(sorted_items[i][0])
            
        return res
        