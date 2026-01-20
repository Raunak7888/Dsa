class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for num in nums:
            isAdded = False
            for i in range(num):
                if (i | (i+1)) == num:
                    ans.append(i)
                    isAdded = True
                    break
            if not isAdded:
                ans.append(-1)
        return ans
                    