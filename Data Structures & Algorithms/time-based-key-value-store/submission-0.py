class TimeMap:

    def __init__(self):
        self.store = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # 如果 key 不存在，直接回傳空字串
        if key not in self.store:
            return res
        
        # 取出該 key 的歷史紀錄列表
        values = self.store[key]
        
        # 進行二分搜尋
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            # 如果 mid 的時間小於等於目標時間，代表這是個候選答案
            if values[mid][0] <= timestamp:
                res = values[mid][1] # 更新答案
                l = mid + 1          # 嘗試往右找，看看有沒有更晚的時間點也符合條件
            else:
                r = mid - 1          # 時間太晚了，往左找
                
        return res
