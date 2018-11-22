class Solution:
    def isSafe(self,x,y,visited):
        if x>=0 and x<len(visited) and y>=0 and y<len(visited[0]) and not(visited[x][y]):
            return True
        return False
    def convert(self,board,visited,x,y):
        visited[x][y]=True
        dx=[-1,0,0,1]
        dy=[0,-1,1,0]
        board[x][y]='-'
        for i in range(4):
            if self.isSafe(x+dx[i],y+dy[i],visited):
                if board[x+dx[i]][y+dy[i]]=='O':
                    self.convert(board,visited,x+dx[i],y+dy[i])
        
                    
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board)==0:
            return
        visited=[[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            if board[i][0]=='O':
                self.convert(board,visited,i,0)
            if board[i][-1]=='O':
                self.convert(board,visited,i,len(board[0])-1)
        for j in range(len(board[0])):
            if board[0][j]=='O':
                self.convert(board,visited,0,j)
            if board[-1][j]=='O':
                self.convert(board,visited,len(board)-1,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='-':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
            
