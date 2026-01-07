class Solution:
    def minChanges(self, n: int, k: int) -> int:
        nb = bin(n)[2:]
        kb = bin(k)[2:]
        if len(nb) >= len(kb):
            kb = "0"*(len(nb)-len(kb)) + kb
        else:
            nb = "0"*(len(kb)-len(nb)) + nb
        print(nb)
        print(kb)
        if kb == nb:
            return 0
        res = 0
        for i in range(len(nb)):
            if nb[i] == '1' and kb[i] == '0':
                res+=1
            if nb[i] == "0" and kb[i] =='1':
                return -1
                
        return res 