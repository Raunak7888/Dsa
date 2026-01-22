class Solution:
    def minimumPairRemoval(self,nums):
        def findMin(nums):
            m = inf
            j = [-1,-1]
            for i in range(len(nums)-1):
                x = nums[i] + nums[i + 1]
                if x < m:
                    m = x
                    j[0]= i
                    j[1] = i+1
            k = nums[j[0]] + nums[j[1]]
            ans = nums[:j[0]]
            ans.append(k)
            ans += nums[j[1]+1:]
            return ans
        res = 0
        i = 0
        while i < len(nums)-1:
            if nums[i] > nums[i+1]:
                nums = findMin(nums)
                # print(nums)
                res +=1
                i=0
            else:
                i+=1
        return res