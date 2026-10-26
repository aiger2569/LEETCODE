class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        
        c = [[0] * n for _ in range(n)]
        for i in range(n):
            c[i][0] = 1
            for j in range(1, i + 1):
                c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD
                
        def dfs(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            l_ways = dfs(left)
            r_ways = dfs(right)
            
            
            comb = c[len(left) + len(right)][len(left)]
            
            return (comb * l_ways % MOD) * r_ways % MOD

        
        return (dfs(nums) - 1 + MOD) % MOD