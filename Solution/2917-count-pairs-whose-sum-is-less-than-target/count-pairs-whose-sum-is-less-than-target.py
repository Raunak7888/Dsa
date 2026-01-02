class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        res = 0
        for i,x in enumerate(nums):
            for j in range(i+1,len(nums)):
                if x + nums[j] < target:
                    res+=1
        return res