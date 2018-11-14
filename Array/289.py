class Solution:
    def isSafe(self,x,y,board):
        if x<0 or y<0 or x>=len(board) or y>=len(board[0]):
            return False
        return True
    def getSum(self,board,x,y):
        direc_x=[-1, -1, -1, 0, 0, 1, 1, 1]
        direc_y=[-1, 0, 1, -1, 1, -1, 0, 1]
        s=0
        for t in range(8):
            #print(x,y,x+direc_x[t],y+direc_y[t])
            if self.isSafe(x+direc_x[t],y+direc_y[t],board):
                s+=board[x+direc_x[t]][y+direc_y[t]]
            
        return s
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        changes=[]
        for i in range(len(board)):
            for j in range(len(board[i])):
                sumOfNeighbours=self.getSum(board,i,j)
                if board[i][j]==0:
                    if sumOfNeighbours==3:
                        changes.append([i,j])
                else:
                    if sumOfNeighbours<2 or sumOfNeighbours>3:
                        changes.append([i,j])
        for change in changes:
            i=change[0]
            j=change[1]
            board[i][j]=1-board[i][j]
        
