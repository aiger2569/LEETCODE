class Solution:
    def minOperations(self, s: str) -> int:
        if s=="".join(sorted(s)):
            return 0
        n=len(s)
        if n==2:
            return -1
        mchar=min(s)
        xchar=max(s)
        if s[0]==mchar or s[-1]==xchar:
            return 1
        fi=s.index(mchar)
        fl=s.rindex(xchar)
        if fi==n-1 and fl==0:
            return 3
        return 2