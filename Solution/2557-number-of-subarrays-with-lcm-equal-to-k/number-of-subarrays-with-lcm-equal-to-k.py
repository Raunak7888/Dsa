import math
from typing import List

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total_count = 0
        def get_lcm(a, b):
            if a == 0 or b == 0:
                return 0
            if a == 1: return b 
            if b == 1: return a
            return (a * b) // math.gcd(a, b)
        
        for i in range(n):
            current_lcm = 1
            for j in range(i, n):
                num_j = nums[j]
                if k % num_j != 0:
                    break 
                if current_lcm == k:
                    total_count += 1
                    continue
                new_lcm = get_lcm(current_lcm, num_j)
                if new_lcm > k:
                    break
                current_lcm = new_lcm
                if current_lcm == k:
                    total_count += 1
        return total_count