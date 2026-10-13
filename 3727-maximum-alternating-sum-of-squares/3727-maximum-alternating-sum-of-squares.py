class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
     
        squares = [x * x for x in nums]
        
       
        squares.sort()
        
        
        mid = len(squares) // 2
        
        return sum(squares[mid:]) - sum(squares[:mid])
