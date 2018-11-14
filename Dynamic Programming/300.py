class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        dp=[1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    dp[j]=max(dp[i]+1,dp[j])
        return max(dp)
