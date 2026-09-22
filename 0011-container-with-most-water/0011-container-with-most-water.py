class Solution:
    def maxArea(self, height: list[int]) -> int:
        n=len(height)
        left=0
        maxcont=0
        right=n-1
        while left<right:
            width=right-left
            eheight=min(height[left],height[right])
            cont=width*eheight
            maxcont=max(maxcont,cont)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxcont