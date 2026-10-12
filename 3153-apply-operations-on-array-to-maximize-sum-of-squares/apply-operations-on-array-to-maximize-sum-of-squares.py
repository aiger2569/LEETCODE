class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        res=0
        m=10**9+7
        count=[0]*30
        for num in nums:
            for i in range(30):
                if num &(1<<i):
                    count[i]+=1
        for _ in range(k):
            cur=0
            for j in range(29,-1,-1):
                if count[j]>0:
                    cur|=1<<j
                    count[j]-=1
            res=(res+cur*cur)%m

        return res