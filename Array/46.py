import copy
class Solution:
    def printPermutations(self,nums,d,l,r):
        if l==r:
            d.append(copy.deepcopy(nums))
        for i in range(l,r+1):
            nums[l],nums[i]=nums[i],nums[l]
            self.printPermutations(nums,d,l+1,r)
            nums[l],nums[i]=nums[i],nums[l]
            
            
        
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [[nums[0]]]
        d=[]
        l=0
        r=len(nums)-1
        for i in range(l,r+1):
            nums[l],nums[i]=nums[i],nums[l]
            self.printPermutations(nums,d,l+1,r)
            nums[l],nums[i]=nums[i],nums[l]
        return d
        
