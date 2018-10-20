class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid)==0:
            return 0
        count=0
        visited=[[False for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.isSafe(grid,visited,i,j):
                    #print(visited[i][j])
                    self.getIsland(grid,visited,i,j)
                    count+=1
        return count
    def isSafe(self,grid,visited,i,j):
        if i<len(grid) and j<len(grid[0]) and i>=0 and j>=0 and not(visited[i][j]) and grid[i][j]=="1":
            return True
        return False
    def getIsland(self,grid,visited,i,j):
        x_direction=[-1,0,0,1]
        y_direction=[0,-1,1,0]
        visited[i][j]=True
        for direc in range(4):
            if self.isSafe(grid,visited,i+x_direction[direc],j+y_direction[direc]):
                self.getIsland(grid,visited,i+x_direction[direc],j+y_direction[direc])
        
