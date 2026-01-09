class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0

        # Traverse from right to left
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue

            parts = (nums[i] + nums[i + 1] - 1) // nums[i + 1]  # ceil division
            res += parts - 1
            nums[i] //= parts
            

        return res
