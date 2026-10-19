class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res=[i for i,x in enumerate(nums) if x==target]
        return res