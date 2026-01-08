class Solution:
    def countpair(self, nums, d):
        left = 0
        count = 0
        for right in range(len(nums)):
            while nums[right]-nums[left] > d:
                left += 1
            count += right-left
        return count        
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = nums[-1]-nums[0]
        while left < right:
            mid = (left+right)//2
            count = self.countpair(nums,mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left
        