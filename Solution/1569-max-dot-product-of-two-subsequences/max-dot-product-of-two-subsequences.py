class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[0]>nums2[0]:
            nums2,nums1=nums1,nums2
        if max(nums1)<0 and min(nums2)>0:
            return max(nums1)*min(nums2)
        m,n=len(nums1),len(nums2)
        d=[0]*(n+1)
        for i in range(m):
            for j in range(n-1,-1,-1):
                v=nums1[i]*nums2[j]+d[j]
                if v>d[j+1]:
                    d[j+1]=v
            for j in range(n):
                if d[j+1]<d[j]:
                    d[j+1]=d[j]
        
        #print(d,d[j+1])
        return d[j+1]