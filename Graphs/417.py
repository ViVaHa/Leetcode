class Solution:
    def isSafe(self,x,y,matrix):
        if x>=0 and x<len(matrix) and y>=0 and y<len(matrix[0]):
            return True
        return False
    def dfs(self,x,y,matrix,canReach):
        if not(self.isSafe(x,y,matrix)):
            return
        canReach[x][y]=True
        dx=[-1,0,0,1]
        dy=[0,1,-1,0]
        for i in range(4):
            if self.isSafe(x+dx[i],y+dy[i],matrix):
                if not(canReach[x+dx[i]][y+dy[i]]) and matrix[x][y]<=matrix[x+dx[i]][y+dy[i]]:
                    self.dfs(x+dx[i],y+dy[i],matrix,canReach)
        
            
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix)==0:
            return []
        pacific=[[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
        atlantic=[[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            pacific[i][0]=True
            atlantic[i][-1]=True
        for j in range(len(matrix[0])):
            pacific[0][j]=True
            atlantic[-1][j]=True
        for i in range(len(matrix)):
            self.dfs(i,0,matrix,pacific)
            self.dfs(i,len(matrix[0])-1,matrix,atlantic)
        for j in range(len(matrix[0])):
            self.dfs(0,j,matrix,pacific)
            self.dfs(len(matrix)-1,j,matrix,atlantic)
        ans=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i,j])
        return ans
        
        
        
