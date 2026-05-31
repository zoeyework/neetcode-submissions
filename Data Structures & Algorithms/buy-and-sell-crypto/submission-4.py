class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_cost=prices[0]
        for price in prices:
            min_cost=min(min_cost,price)
            current_profit=price-min_cost
            max_profit=max(max_profit,current_profit)
        return max_profit