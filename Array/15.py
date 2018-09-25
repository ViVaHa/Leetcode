class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        outer=[]
        nums.sort()
        if len(nums)==0:
            return []
        for index in range(len(nums)):
            if index>0 and nums[index]==nums[index-1]:
                continue
            i=index+1
            j=len(nums)-1
            while i<j:
                if nums[i]+nums[j]+nums[index]==0:
                    inner=[nums[i],nums[index],nums[j]]
                    outer.append(inner)
                    while i+1<len(nums) and nums[i]==nums[i+1]:
                        i+=1
                    while j-1>0 and nums[j]==nums[j-1]:
                        j-=1
                    i+=1
                    j-=1
                elif nums[i]+nums[j]+nums[index]<0:
                    i+=1
                else:
                    j-=1
        
        return outer
