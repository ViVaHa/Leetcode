class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0:
            return []
        ans=[]
        if len(matrix)==1:
            for i in range(len(matrix[0])):
                ans.append(matrix[0][i])
            return ans
        if len(matrix[0])==1:
            for i in range(len(matrix)):
                ans.append(matrix[i][0])
            return ans
        direction="right"
        left=0
        top=0
        right=len(matrix[0])-1
        bottom=len(matrix)-1
        i=0
        j=0
        while top<=bottom and left<=right:
            for j in range(left,right+1):
                ans.append(matrix[top][j])
                #print(matrix[top][j])
            top+=1
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
                #print(matrix[i][right])
            right-=1
            if top<=bottom:
                for j in range(right,left-1,-1):
                    ans.append(matrix[bottom][j])
                    #print(matrix[bottom][j])
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1
        return ans
                    
        
