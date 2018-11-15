class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        sortedDict=sorted(d, key=d.get, reverse=True)
        ans=[]
        for i in range(k):
            ans.append(sortedDict[i])
        return ans
            
        
