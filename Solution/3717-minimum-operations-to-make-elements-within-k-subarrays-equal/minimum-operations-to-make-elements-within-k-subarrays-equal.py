class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:

        n = len(nums)

        l_size = x // 2
        r_size = x - l_size

        init = sorted([(num, i) for i, num in enumerate(nums[:x])])
        mid = init[l_size][0]

        left, right = [], []
        cost = 0
        for idx in range(x):
            num, i = init[idx]
            cost += abs(num - mid)
            
            if idx < l_size:
                heapq.heappush(left, (-num, -i))
            else:
                heapq.heappush(right, (num, i))

        costs = [float('inf')] * x + [cost]

        for i in range(x, n):
            old, new = nums[i-x], nums[i]
            
            is_old_left = False
            if old < right[0][0] or (old == right[0][0] and i-x < right[0][1]):
                is_old_left = True

            if is_old_left:
                while left and -left[0][1] <= i-x:
                    heapq.heappop(left)

                cost -= abs(old - mid)
                cost += abs(new - mid)
                    
                if new < right[0][0]:
                    
                    heapq.heappush(left, (-new, -i))

                else:
                   
                    pop_right, pop_right_i = heapq.heappop(right)
                    while right and right[0][1] <= i-x:
                        heapq.heappop(right)

                    heapq.heappush(left, (-pop_right, -pop_right_i))
                    heapq.heappush(right, (new, i))

                    cost += l_size * abs(right[0][0] - mid)
                    cost -= r_size * abs(right[0][0] - mid)
                    mid = right[0][0]

            else:
                while right and right[0][1] <= i-x:
                    heapq.heappop(right)

                cost -= abs(old - mid)
                cost += abs(new - mid)

                if new >= -left[0][0]:
                    
                    heapq.heappush(right, (new, i))
                    if mid < right[0][0]:
                        cost += l_size * abs(right[0][0] - mid)
                        cost -= r_size * abs(right[0][0] - mid)
                    else:
                        cost -= (l_size + 1) * abs(right[0][0] - mid)
                        cost += (r_size - 1) * abs(right[0][0] - mid)
                    mid = right[0][0]

                else:
                    
                    pop_left, pop_left_i = heapq.heappop(left)
                    pop_left, pop_left_i = -pop_left, -pop_left_i

                    while left and -left[0][1] <= i-x:
                        heapq.heappop(left)

                    heapq.heappush(left, (-new, -i))
                    heapq.heappush(right, (pop_left, pop_left_i))

                    cost -= abs(mid - pop_left)
                    cost += (r_size - 1) * abs(mid - pop_left)
                    cost -= l_size * abs(mid - pop_left)
                    mid = pop_left
            
            costs.append(cost)

        dp = [float('inf')]
        for i in range(n):
            dp.append(min(dp[-1], costs[i+1]))

        for _ in range(1, k):
            ndp = [float('inf')] * x
            for i in range(x, n+1):
                ndp.append(min(ndp[-1], dp[i-x] + costs[i]))

            dp = ndp
        return dp[-1]
        