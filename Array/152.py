class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        mx=nums[0]
        mn=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>0:
                mx=max(nums[i],nums[i]*mx)
                mn=min(nums[i],nums[i]*mn)
            else:
                tmp=mx
                mx=max(nums[i],nums[i]*mn)
                mn=min(nums[i],nums[i]*tmp)
            if mx>ans:
                ans=mx
        return ans
        
