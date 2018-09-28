class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==0:
            return False
        if nums[0]==0 and len(nums)>1:
            return False
        lastPosition=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=lastPosition:
                lastPosition=i
        #print(lastPosition)
        if lastPosition<=0:
            return True
        else:
            return False
