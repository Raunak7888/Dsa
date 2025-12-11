class Solution:
    def canJump(self, nums: List[int]) -> bool:
        print(len(nums))
        print(nums[0])
        if len(nums) == 1:
            return True
        far = 0
        for i,num in enumerate(nums):
            if i>far:
                return False
            far = max(far,i+num)
        return True if far else False 
        
    