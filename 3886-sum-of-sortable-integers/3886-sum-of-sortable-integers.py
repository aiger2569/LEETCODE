class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        
        prefMax = [0] * (n + 1)
        curr_max = -10**18
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            prefMax[i + 1] = curr_max
            
        
        suffMin = [10**18] * (n + 1)
        curr_min = 10**18
        for i in range(n - 1, -1, -1):
            curr_min = min(curr_min, nums[i])
            suffMin[i] = curr_min
            
        
        prefDrop = [0] * n
        for i in range(1, n):
            prefDrop[i] = prefDrop[i - 1] + (1 if nums[i - 1] > nums[i] else 0)
            
        
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
                    
        total_sum = 0
        
        for k in divisors:
            is_sortable = True
            for start in range(0, n, k):
                end = start + k
                
                if start > 0 and prefMax[start] > suffMin[start]:
                    is_sortable = False
                    break
                    
                
                internal_drops = prefDrop[end - 1] - prefDrop[start] if end - 1 > start else 0
                circular_drop = 1 if nums[end - 1] > nums[start] else 0
                total_drops = internal_drops + circular_drop
                
                if total_drops > 1:
                    is_sortable = False
                    break
                    
            if is_sortable:
                total_sum += k
                
        return total_sum