class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        seen = {}
        res = 0
        for end,ch in enumerate(s):
            if ch in seen and seen[ch] >= start:
                start = seen[ch]+1
            seen[ch] = end
            res = max(res,end-start+1)
        return res