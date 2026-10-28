'''class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        c=grid[n-1][m-1]
        a,b=0,0
        s=0
        print(m,n,c)
        for i in range(n-1,0,-1):
            for j in range(m-1,0,-1):
                a=c^grid[i-1][j]
                b=c^grid[i][j-1]
                if b>a:
                    c=grid[i-1][j]
                    s+=a
                else:
                    c=grid[i][j-1]
                    s+=b
        return s'''
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        # dp[i][j] will store a set of all possible XOR values to reach cell (i, j)
        dp = [[set() for _ in range(m)] for _ in range(n)]
        
        # Base case: starting point has exactly one possible XOR value
        dp[0][0].add(grid[0][0])
        
        # Fill the DP table
        for i in range(n):
            for j in range(m):
                # If we can come from the top cell
                if i > 0:
                    for prev_xor in dp[i-1][j]:
                        dp[i][j].add(prev_xor ^ grid[i][j])
                
                # If we can come from the left cell
                if j > 0:
                    for prev_xor in dp[i][j-1]:
                        dp[i][j].add(prev_xor ^ grid[i][j])
        
        # Return the smallest XOR sum accumulated at the bottom-right corner
        return min(dp[n-1][m-1])
