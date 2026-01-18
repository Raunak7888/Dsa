class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        totalsum = sum(nums)
        lsum = 0
        for i in range(n):
            if lsum == totalsum-lsum-nums[i]:
                return i
            lsum+=nums[i]
        return -1