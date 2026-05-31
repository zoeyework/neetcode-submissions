class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        max_profit = 0
        min_price = prices[0]
        for i in range(len(prices)):
            if i == 0:
                min_price=prices[i]
            else:
                min_price=min(prices[i-1], min_price)
            current_profit = prices[i] - min_price
            max_profit=max(max_profit,current_profit)
        return max_profit      

        