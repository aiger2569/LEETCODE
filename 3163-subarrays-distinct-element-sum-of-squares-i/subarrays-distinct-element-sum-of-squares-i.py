class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        es=0
        n=len(nums)
        for i in range(n):
            lset=set()
            for j in range(i,n):
                lset.add(nums[j])
                es+=len(lset)**2
        return es