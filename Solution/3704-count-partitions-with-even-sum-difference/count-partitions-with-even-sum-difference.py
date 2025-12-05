class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-1):
            # print(nums[:i+1],"               ",nums[i+1:])
            # print()
            if (sum(nums[:i+1])- sum(nums[i+1:]))%2==0:
                res+=1
        return res
            