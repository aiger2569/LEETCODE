class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        s=0
        for i in range(len(nums)):
            if len(nums)%(i+1)==0:
                s+=nums[i]**2
        return s
        