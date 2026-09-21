from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d=defaultdict(list)
        for words in strs:
            c=[0]*26
            for char in words:
                c[ord(char)-ord('a')]+=1
            c=tuple(c)
            d[c].append(words)             
        return list(d.values())
        