from typing import List

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        # The largest allowed value for the current element's last part.
        bound = nums[-1]
        operations = 0
        
        # Process from right to left.
        for i in range(n - 2, -1, -1):
            x = nums[i]
            if x <= bound:
                bound = x
            else:
                k = (x + bound - 1) // bound
                operations += k - 1  # each split adds one piece.
                bound = x // k
        
        return operations
