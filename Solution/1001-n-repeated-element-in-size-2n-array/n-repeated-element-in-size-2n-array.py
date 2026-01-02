class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        l = Counter(nums)
        n = len(nums)//2
        for i in l.keys():
            if l[i] >= n:
                return i
        return -1