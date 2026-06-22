class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        greatest_diff = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                if profit > greatest_diff:
                    greatest_diff = profit
            else:
                l = r
            r += 1
        return greatest_diff
