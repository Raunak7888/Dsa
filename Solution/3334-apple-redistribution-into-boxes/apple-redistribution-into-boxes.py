class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        a = sum(apple)
        res = 0
        capacity.sort(reverse = True)
        for i in capacity:
            if a <= 0:
                break
            a-=i
            res+=1
        return res