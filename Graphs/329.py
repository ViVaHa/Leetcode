class Solution:
    dp=None
    def isSafe(self,x,y,matrix):
        if x>=0 and y>=0 and x<len(matrix) and y<len(matrix[0]):
            return True
        return False
    def dfs(self,matrix,x,y):
        if not(self.isSafe(x,y,matrix)):
            return 0
        if self.dp[x][y] is not None:
            return self.dp[x][y]
        x_direc=[-1,0,0,1]
        y_direc=[0,-1,1,0]
        val=-sys.maxsize
        for i in range(4):
            if self.isSafe(x+x_direc[i],y+y_direc[i],matrix):
                if matrix[x+x_direc[i]][y+y_direc[i]]>matrix[x][y]:
                    val=max(val,self.dfs(matrix,x+x_direc[i],y+y_direc[i]))
                else:
                    val=max(val,0)
        self.dp[x][y]=max(val+1,1)
        return max(val+1,1)
                    
                    
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix)==0:
            return 0
        val=-sys.maxsize
        self.dp=[[None for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val=max(val,self.dfs(matrix,i,j))
        return val
