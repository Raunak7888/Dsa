class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sm = Counter(s)
        tm = Counter(t)
        res = 0
        for i in "abcdefghijklmnopqrstuvwxyz":
            res += abs(sm[i]-tm[i])
        return res//2