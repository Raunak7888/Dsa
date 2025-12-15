class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)
        count = 0
        for c in range(2, n - 1):
            b = c - 1
            for a in range(b):
                freq[nums[a] + nums[b]] += 1
            for d in range(c + 1, n):
                count += freq[nums[d] - nums[c]]

        return count
