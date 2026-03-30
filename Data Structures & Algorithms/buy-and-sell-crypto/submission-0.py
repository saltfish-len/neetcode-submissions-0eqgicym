class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=101
        profit = 0
        for i in range(len(prices)-1):
            
            buy = min(buy,prices[i])
            profit = max(profit,prices[i+1]-buy)

        return profit