class Solution:
    def isValid(self,board,i,j,number):
        if board[i][j]==".":
            return True
        col=[0 for x in range(len(board))]
        for x in range(len(board)):
            col[x]=board[x][j]
        row=board[i]
        if row.count(number)>1 or col.count(number)>1:
            print(number)
            return False
        row = i-(i%3)
        col=j-(j%3)
        for k in range(0,3):
            for l in range(0,3):
                if board[row+k][col+l]==number:
                    if not(row+k==i and col+l==j):
                        return False
        return True
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board)==0:
            return False
        count=0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.isValid(board,i,j,board[i][j]):
                    count+=1
        if count==len(board)*len(board[0]):
            return True
        return False
