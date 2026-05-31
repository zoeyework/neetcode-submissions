class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap={}
        for i, n in enumerate(nums):
            diff = target - n
            print('diff',diff)
            if diff in preMap:   #如果差異數在 premap 字典裡 return 
                print('preMap[diff]', preMap[diff])
                return [preMap[diff], i]
            preMap[n]=i
        return

'''
#第一次 
i=0, n=3
diff=4
preMap[3]=0 
preMap={'3':0}
#第二次
i=1, n=4
diff=3
diff 有在 preMap
return 0,1 

'''