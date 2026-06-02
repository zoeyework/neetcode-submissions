from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 當石頭堆裡還有至少 2 顆石頭時，就繼續撞擊
        while len(stones) > 1:
            stones.sort()  # 1. 每次都重新排序，從小到大
            
            x = stones.pop()  # 2. 取出當前最重的石頭（最後一項）
            y = stones.pop()  # 3. 取出當前第二重的石頭（倒數第二項）
            
            if x != y:
                # 4. 如果兩顆石頭重量不同，將差值（碎渣）放回陣列中
                # 因為前面排過序，x 必定大於或等於 y，所以直接 x - y 即可
                stones.append(x - y)
        
        # 如果最後剛好撞光了（陣列空了），回傳 0；還剩一顆就回傳該顆石頭重量
        return stones[0] if stones else 0

