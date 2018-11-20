class Solution:
    mem=None
    def dfs(self,nums,index,S):
        if index>len(nums):
            return 0
        if S==0 and index==len(nums):
            return 1
        if index==len(nums) and S!=0:
            return 0
        if (index,S) in self.mem:
            return self.mem[(index,S)]
        else:
            x=self.dfs(nums,index+1,S-nums[index])
            x+=self.dfs(nums,index+1,S+nums[index])
            self.mem[(index,S)]=x
            return x
        
        
        
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        symbol=0
        self.mem={}
        count=self.dfs(nums,1,S-nums[0])
        count+=self.dfs(nums,1,S+nums[0])
        return count
        
