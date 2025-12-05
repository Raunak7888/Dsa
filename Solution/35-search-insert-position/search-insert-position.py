class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start<=end:
            mid = (start+end)//2
            
            if nums[mid] < target:
                start = mid + 1
            else:
                end = end-1
        return start