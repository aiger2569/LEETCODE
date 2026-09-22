class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        profit=0
        currentprofit=0
        maxprofit=0
        left=0
        for right in range(1,len(prices)):
            if prices[right]>prices[left]:
                currentprofit=prices[right]-prices[left]
                maxprofit=max(maxprofit,currentprofit)
            else: left=right
        return maxprofit