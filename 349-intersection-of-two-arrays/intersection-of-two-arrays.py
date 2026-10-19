class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        SET=set(nums2)
        return list(set(i for i in nums1 if i in SET))