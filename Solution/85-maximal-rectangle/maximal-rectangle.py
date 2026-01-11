class Solution:
    def maximalRectangle(self, g: List[List[str]]) -> int:
        return max(map(self.largestRectangleArea,
            zip(*(accumulate(map(int,r),lambda p,v:v*-~p) for r in g))))
        # 84. Largest Rectangle in Histogram
    def largestRectangleArea(self, a: List[int]) -> int:
        a += (0,) # force stack to pop all at the end
        g = lambda q,v,j,res:q[0]>=v and g(q[3],v,j+q[1],max(res,q[0]*(j+q[1]),q[2])) \
            or [v,j+1,max(res,v*(j+1),q[2]),q]
        return (f:=lambda q,i:i<len(a) and f(g(q,a[i],0,0),i+1) or q)([-1,0,0,[]],0)[2]
        #                                                               ^ ^ ^ ^
        #                                                               0 1 2 3
        # 0 - cur stack value, 1 - counter, 2 - result, 3 - stack implementation