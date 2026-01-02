class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        nums[-1] +=1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > 9:
                nums[i] = nums[i]%10 
                nums[i-1] +=1
        if nums[0] > 9:
            nums[0] = nums[0]%10
            nums.insert(0,1)
        return nums