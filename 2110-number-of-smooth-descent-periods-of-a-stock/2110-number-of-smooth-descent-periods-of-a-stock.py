class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        t=1
        s=1
        for i in range(1,len(prices)):
            if prices[i-1]-1==prices[i]:
                s+=1
            else:
                s=1
            t+=s
        return t
