import sys
import copy
class Solution:
    def generateSubsets(self,nums,i,temp,res):
        if i==len(nums):
            res.append(copy.deepcopy(temp))
            return
        temp.append(nums[i])
        self.generateSubsets(nums,i+1,temp,res)
        temp.pop()
        self.generateSubsets(nums,i+1,temp,res)
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums)==0:
            return []
        temp=[]
        res=[]
        self.generateSubsets(nums,0,temp,res)
        return res
