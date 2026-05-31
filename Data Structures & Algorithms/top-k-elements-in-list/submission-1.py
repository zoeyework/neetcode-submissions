class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for n in nums:
            count[n]=1+count.get(n,0)
            #count[n] = 1 + count[n].get(n, 0)
        sorted_count_des =sorted(count.items(), key=lambda x: x[1], reverse=True)
        res=[]
        for i in range(k):
            print(sorted_count_des[i][0])
            res.append(sorted_count_des[i][0])
        return res

'''
nums=[7,7]
k=1

round 1 :
count={7:1}
rount 2:
count={7:2}
'''



        