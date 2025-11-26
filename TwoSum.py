from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    dic = {}
    for i,num in enumerate(nums):
        if target - num in dic:
            return [dic[target - num], i]
        else:
            dic[num] = i
    return [-1,-1]

if __name__ == '__main__':
    print(two_sum([2,7,11,15], 9))
    print(two_sum([3,2,4], 9))
    print(two_sum([3,3], 6))

