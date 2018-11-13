class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if len(nums)==0:
            return 
        white=0
        red=0
        blue=len(nums)-1
        while white<=blue:
            if nums[white]==1:
                white+=1
            elif nums[white]==2:
                nums[white],nums[blue]=nums[blue],nums[white]
                blue-=1
            else:
                nums[white],nums[red]=nums[red],nums[white]
                white+=1
                red+=1
        
                
    
                
