class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        i=len(matrix)-1
        j=0
        while i>-1 and j<len(matrix[0]):
            if matrix[i][j]<target:
                j+=1
            elif matrix[i][j]>target:
                i-=1
            else:
                return True
            #print(i,j)
        return False
        
