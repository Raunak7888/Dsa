class Solution:
    def minimumAbsDifference(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 2:
            return [[nums[0],nums[1]]]
        nums.sort()
        
        res = []
        k = inf
        ans = []
        for i in range(len(nums)-1):
            j = abs(nums[i]-nums[i+1])
            if j < k:
                k = j
                # ans = [nums[i],nums[i+1]]
        # res.append(ans)
        for i in range(len(nums)):
            j = abs(nums[i]-nums[i-1])
            if j == k:
                res.append([nums[i-1],nums[i]])
        return res
