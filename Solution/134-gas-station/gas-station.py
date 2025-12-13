class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        res = 0
        tg = 0
        for i,g in enumerate(gas):
            fuel = g-cost[i]
            tank += fuel
            tg += fuel
            if tank < 0:
                res = i+1
                tank = 0
        return -1 if tg < 0 else res

