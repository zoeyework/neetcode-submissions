class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. 把位置跟速度合體，並按照「位置」由大到小排序
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for p, s in cars:
            time = (target - p) / s
            
            # 2. 如果這台車「比前方的車隊領隊慢」，它就是一個新車隊
            if not stack or time > stack[-1]:
                stack.append(time)
            
            # 如果它比前方領隊快 (time <= stack[-1])，就代表它會併入
            # 我們什麼都不用做，因為它會被前面的車擋住，時間變長
            
        return len(stack)