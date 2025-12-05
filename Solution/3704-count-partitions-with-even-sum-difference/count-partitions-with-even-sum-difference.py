class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        res = 0
        f = nums[0]
        s = sum(nums[1:])
        if ((f-s)%2 == 0):
            res+=1
        for i in range(1,(len(nums)-1)):
            f += nums[i]
            s -= nums[i]
            if (f-s) % 2 == 0:
                res+=1
        return res
            