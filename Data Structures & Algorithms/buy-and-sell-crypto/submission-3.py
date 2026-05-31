class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            # Update the lowest price we've seen so far
            min_price = min(min_price, price)
            # Calculate profit if we sold today and update global max
            max_profit = max(max_profit, price - min_price)
        return max_profit      

        