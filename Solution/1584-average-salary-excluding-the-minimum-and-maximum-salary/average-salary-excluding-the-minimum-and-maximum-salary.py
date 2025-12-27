class Solution:
    def average(self, nums: List[int]) -> float:
        mx = 0
        mi = 10000000
        avg = 0
        for i in nums:
            avg+=i
            mx = max(i,mx)
            mi = min(i,mi)
        
        return (avg-mx-mi)/(len(nums)-2)