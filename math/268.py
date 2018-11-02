class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        sums=0
        for i in range(len(nums)):
            sums+=nums[i]
            if nums[i]>l:
                l=nums[i]
        l=max(len(nums),l)
        s=l*(l+1)
        s=int(s/2)
        return s-sums
