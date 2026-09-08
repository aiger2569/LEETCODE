class Solution:
    def countCommas(self, n: int) -> int:
        a=str(n)
        if n<1000:
            return 0
        return n-999
        
