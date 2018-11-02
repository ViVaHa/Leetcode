class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d={}
        for i in range(len(nums1)):
            if nums1[i] in d:
                d[nums1[i]]+=1
            else:
                d[nums1[i]]=1
        ans=[]
        for i in range(len(nums2)):
            if nums2[i] in d and d[nums2[i]]>0:
                ans.append(nums2[i])
                d[nums2[i]]-=1
        return ans
                
        
