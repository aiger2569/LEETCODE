class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res=[]
        c=0
        i,j=len(num1)-1,len(num2)-1
        while i>=0 or j>=0 or c:
            d1=ord(num1[i])-ord('0') if i>=0 else 0
            d2=ord(num2[j])-ord('0')if j>=0 else 0
            t=d1+d2+c
            c=t//10
            res.append(chr(t%10+ord('0')))
            i-=1
            j-=1
        return ''.join(res[::-1])