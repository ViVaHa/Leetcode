class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)==0:
            return 0
        left=[0]*len(height)
        right=[0]*len(height)
        i=0
        left[i]=height[i]
        while i<len(height):
            left[i]=max(left[i-1],height[i])
            i+=1
        i=len(height)-2
        right[-1]=height[-1]
        while i>=0:
            right[i]=max(right[i+1],height[i])
            i-=1
        i=0
        res=0
        while i<len(height):
            res+=min(left[i],right[i])-height[i]
            i+=1
        return res
            
