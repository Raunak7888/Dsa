class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        m = set()
        for i in range(len(nums)-1,-1,-1):
            if len(m) == 0:
                m.add(nums[i])
            elif nums[i] in m:
                up = i+1
                return math.ceil(up/3)
            else:
                m.add(nums[i])
        return 0