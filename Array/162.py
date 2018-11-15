class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return -1
        if len(nums)==1:
            return 0
        if len(nums)==2:
            m=0
            for i in range(2):
                if nums[m]<nums[i]:
                    m=i
            return m
        start=0
        end=len(nums)-1
        while start<end:
            mid=(start+end)//2
            if nums[mid]>=nums[mid+1]:
                end=mid
            else:
                start=mid+1
        return start
                
        
