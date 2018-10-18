class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        res=matrix
        n=len(matrix)
        for i in range(len(matrix)//2):
            for j in range(i,n-i-1):
                temp=res[i][j]
                res[i][j]=res[j][n-i-1]
                res[j][n-i-1]=res[n-i-1][n-j-1]
                res[n-i-1][n-j-1]=res[n-j-1][i]
                res[n-j-1][i]=temp
        matrix=res
        for row in matrix:
            row.reverse()
        for i in range(len(matrix)//2):
            j=n-i-1
            matrix[i],matrix[j]=matrix[j],matrix[i]
        
