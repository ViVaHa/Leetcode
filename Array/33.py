class Solution:
    def binarySearch(self,start,end,nums,target):
        if start>end:
            return -1
        while start<=end:
            mid=start+int((end-start+1)/2)
            if nums[mid]==target:
                return mid
            if nums[start]<=nums[mid]:
                if nums[start]<=target and target<=nums[mid]:
                    end=mid-1
                else:
                    start=mid+1
            else:
                if nums[mid]<=target and target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1
        return -1
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        mid=int((len(nums))/2)
        index=self.binarySearch(0,len(nums)-1,nums,target)
        return index
