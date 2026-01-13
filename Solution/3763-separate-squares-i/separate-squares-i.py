class Solution:
    def separateSquares(self, nums: List[List[int]]) -> float:
        low,high,area = float(inf), float(-inf),0
        for x,y,l in nums:
            area += l*l
            low = min(low,y)
            high = max(high,y+l)
        
        area = area /2.0

        for i in range(60):
            mid = (low+high)/2.0

            curr_area = 0
            for _,y,l in nums:
                curr= max(0,min(l,mid-y))
                curr_area += l*curr
            
            if curr_area < area:
                low = mid
            else:
                high = mid
        return mid