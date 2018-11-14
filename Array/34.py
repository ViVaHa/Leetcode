class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return [-1,-1]
        ans=[]
                
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            #print(mid)
            if nums[mid]<target:
                start=mid+1
            elif nums[mid]>target:
                end=mid-1
            else:
                if (mid-1>=start and nums[mid-1]<target) or start==end:
                    ans.append(mid)
                    break
                else:
                    end=mid
        if end<start:
            ans.append(-1)
        
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            #print(mid)
            if nums[mid]<target:
                start=mid+1
            elif nums[mid]>target:
                end=mid-1
            else:
                if (mid+1<=end and nums[mid+1]>target) or start==end:
                    ans.append(mid)
                    break
                else:
                    start=mid+1
        if end<start:
            ans.append(-1)
        
        return ans
        
        
        
        '''          
            
        if end<start:
            ans.append(-1)
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            
        if end<start:
            ans.append(-1)
        return ans
        '''
        
