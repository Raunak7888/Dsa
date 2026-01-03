class Solution:
    def numOfWays(self,n: int) -> int:
        MOD = 10**9 + 7

        A = 6  
        B = 6  

        for _ in range(1, n):
            newA = (3 * A + 2 * B) % MOD
            newB = (2 * A + 2 * B) % MOD
            A, B = newA, newB

        return (A + B) % MOD
