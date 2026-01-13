class Solution:
    def minOperations(self, nums: List[int]) -> int:
        seen = set()

        cnt = 0
        for num in reversed(nums):

            if num not in seen:
                cnt += 1
                seen.add(num)
            else:
                break

        n = len(nums)
        need_remove = n - cnt
        return math.ceil(need_remove / 3)