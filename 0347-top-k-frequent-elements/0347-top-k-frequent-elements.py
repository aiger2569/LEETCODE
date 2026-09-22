from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        c=Counter(nums)
        print(c)
        return[ item[0]for item in c.most_common(k)]