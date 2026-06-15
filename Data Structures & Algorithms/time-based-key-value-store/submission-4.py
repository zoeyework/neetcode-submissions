import bisect

class TimeMap:
    def __init__(self):
        # 結構: {key: [(timestamp1, value1), (timestamp2, value2), ...]}
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        arr = self.store[key]
        
        # 使用二分搜尋找到符合 <= timestamp 的最大索引
        # bisect_right 會回傳「第一個大於 timestamp 的位置」
        idx = bisect.bisect_right(arr, (timestamp, chr(127)))
        
        if idx == 0:
            return ""
        
        # 回傳索引前一個的 value
        return arr[idx - 1][1]

