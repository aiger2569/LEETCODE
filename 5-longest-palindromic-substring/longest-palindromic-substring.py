class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        m="@"
        for c in s:
            m+="#"+c
        m+="#$"
        b=len(m)
        p=[0]*b
        l,r=0,0
        for i in range(1,b-1):
            if i<r:
                mirror=l+r-i
                p[i]=min(r-i,p[mirror])
            while i-1-p[i]>=0 and i+1+p[i]<b and m[i-1-p[i]]==m[i+1+p[i]]:
                p[i]+=1
            if i + p[i] > r:
                l = i - p[i]
                r = i + p[i]
        maxlen=1
        start=0
        for i in range(1, b- 1):
            if p[i] > maxlen:
                maxlen = p[i]
                start = (i - p[i]) // 2
        return s[start:start+maxlen]
