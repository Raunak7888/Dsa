class Solution:
    def longestCommonSubsequence(self,s1, s2):
        n, m = len(s1), len(s2)
        dp = [0] * (m+1)

        for i in range(1, n+1):
            prevDiag = 0
            for j in range(1, m+1):
                temp = dp[j]
                if s1[i-1] == s2[j-1]:
                    dp[j] = 1 + prevDiag
                else:
                    dp[j] = max(dp[j], dp[j-1])
                prevDiag = temp

        return dp[m]
