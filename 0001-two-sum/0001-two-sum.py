class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mat = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mat:
                return [mat[diff], i]
            mat[n] = i
