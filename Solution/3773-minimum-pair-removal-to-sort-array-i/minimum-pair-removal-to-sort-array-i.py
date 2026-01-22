from math import inf

class Solution:
    def minimumPairRemoval(self, nums):
        def is_sorted(arr):
            return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

        def merge_min_pair(arr):
            min_sum = inf
            idx = 0

            for i in range(len(arr) - 1):
                s = arr[i] + arr[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            return arr[:idx] + [min_sum] + arr[idx + 2:]

        operations = 0

        while not is_sorted(nums):
            nums = merge_min_pair(nums)
            operations += 1

        return operations
