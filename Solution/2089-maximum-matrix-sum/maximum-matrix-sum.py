class Solution:
    def maxMatrixSum(self, m: List[List[int]]) -> int:
        n = len(m)
        res = 0
        minVal = 9999999
        r = 0
        for i in range(n):
            for j in range(n):
                res += abs(m[i][j])
                minVal = min(minVal, abs(m[i][j]))
                if m[i][j]<0:
                    r+=1
        print(res,minVal,r)
        if r%2==0:
            return res
        else: 
            return res-minVal*2
