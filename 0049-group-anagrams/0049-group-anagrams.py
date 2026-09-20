from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d=defaultdict(list)
        for words in strs:
            d["".join(sorted(words))].append(words)             
        return list(d.values())
        