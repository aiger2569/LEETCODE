class Solution:
    def romanToInt(self, s: str) -> int:
        rmap={"I":1,"V":5,"C":100,"X":10,"D":500,"M":1000,"L":50}
        total=0
        for i in range(len(s)):
            if i<len(s)-1 and rmap[s[i]]<rmap[s[i+1]]:
                total-=rmap[s[i]]
            else:
                total+=rmap[s[i]] 
        return total 
        