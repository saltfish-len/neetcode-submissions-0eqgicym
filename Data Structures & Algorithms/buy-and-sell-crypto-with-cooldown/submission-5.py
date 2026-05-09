class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        NEG = float('-inf')
        hold = [NEG for _ in range(n+1)] # max profit end in i and holding stock
        sold = [NEG for _ in range(n+1)] # max profit end in i and selling on i
        buy = [0 for _ in range(n+1)] # max profit end in i and can buy on i

        for i in range(1, n+1):
            hold[i] = max(hold[i-1],buy[i-1]-prices[i-1])
            sold[i] = hold[i-1] + prices[i-1]
            buy[i] = max(buy[i-1], sold[i-1])
        return max(sold[n], buy[n])
        