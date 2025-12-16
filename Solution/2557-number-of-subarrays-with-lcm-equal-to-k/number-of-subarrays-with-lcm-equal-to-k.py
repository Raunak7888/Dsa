from math import lcm


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:

        n = len(nums)

        num_subarrays = 0
        first = 0
        first_in_run = first
        last = first
        lcm_prefix = [1]
        lcm_suffix = None
        while last < n:
            if k % nums[last] != 0:
                first = last + 1
                while first < n:
                    if k % nums[first] == 0:
                        break
                    first += 1
                else:
                    return num_subarrays
                first_in_run = first
                last = first
                lcm_prefix = [1]
                lcm_suffix = None

            else:
                lcm_prefix.append(lcm(lcm_prefix[-1], nums[last]))
                if lcm_prefix[-1] == k:
                    first = last
                    lcm_suffix = [nums[first]]
                    while lcm_suffix[-1] != k:
                        first -= 1
                        lcm_suffix.append(lcm(lcm_suffix[-1], nums[first]))
                    num_subarrays += first - first_in_run + 1
                    print(num_subarrays, first, first_in_run)

                last += 1

        return num_subarrays




    def subarrayLCM2(self, nums: List[int], k: int) -> int:

        n = len(nums)

        num_subarrays = 0

        first = 0
        while first < n:
            if k % nums[first] == 0:
                break
            first += 1
        else:
            return num_subarrays
        first_in_run = first
        last = first + 1
        lcm_prefix = [nums[first]]
        lcm_suffix = None

        while last < n:
            if k % nums[last] != 0:
                first = last + 1
                while first < n:
                    if k % nums[first] == 0:
                        break
                    first += 1
                else:
                    return num_subarrays
                first_in_run = first
                last = first
                lcm_prefix = [1]
                lcm_suffix = None

            else:
                lcm_prefix.append(lcm(lcm_prefix[-1], nums[last]))
                if lcm_prefix[-1] == k:
                    first = last
                    lcm_suffix = [nums[first]]
                    while lcm_suffix[-1] != k:
                        first -= 1
                        lcm_suffix.append(lcm(lcm_suffix[-1], nums[first]))
                    num_subarrays += first - first_in_run + 1
                    print(num_subarrays, first, first_in_run)


                    #first += 1
                    #if first > last:
                    #    while first < n:
                    #        if k % nums[first] == 0:
                    #            break
                    #        first += 1
                    #    else:
                    #        return num_subarrays
                    #    if first > last + 1:
                    #        first_in_run = first
                    #    last = first
                    #    lcm_prefix = [nums[first]]
                    #else:
                    #lcm_prefix = [lcm_suffix[-2]]
                last += 1
        
        if lcm_prefix[-1] == k:
            first = last - 1
            lcm_suffix = [nums[first]]
            while lcm_suffix[-1] != k:
                first -= 1
                lcm_suffix.append(lcm(lcm_suffix[-1], nums[first]))
            num_subarrays += first - first_in_run + 1
            print(num_subarrays, first, first_in_run)

        return num_subarrays