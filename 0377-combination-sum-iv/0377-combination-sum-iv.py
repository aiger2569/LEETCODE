class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        c=[0]*(target+1)
        c[0]=1
        for i in range(1,target+1):
            for num in nums:
                if  i-num>=0:
                    c[i]+=c[i-num]
        return c[target]
      
        