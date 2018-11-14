class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==0:
            return False
        m1=sys.maxsize
        m2=sys.maxsize
        for num in nums:
            if num<=m1:
                m1=num
            elif num<=m2:
                m2=num
            else:
                return True
        return False
        
