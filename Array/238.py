class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return 
        productSoFar=1
        ans=[1 for i in range(len(nums))]
        for i in range(0,len(nums)):
            ans[i]=productSoFar
            productSoFar*=nums[i]
        productSoFar=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=productSoFar
            productSoFar*=nums[i]
        return ans
