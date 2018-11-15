class Solution:
    def isSafe(self,x,y,letter,visited,board):
        if x<0 or y<0 or x>=len(visited) or y>=len(visited[0]) or visited[x][y] or board[x][y]!=letter:
            return False
        return True
        
    def find(self,board,word,x,y,index,visited):
        if index==len(word):
            return True
        letter=word[index]
        visited[x][y]=True
        x_direc=[-1,0,0,1]
        y_direc=[0,-1,1,0]
        for i in range(4):
            if self.isSafe(x+x_direc[i],y+y_direc[i],letter,visited,board):
                if self.find(board,word,x+x_direc[i],y+y_direc[i],index+1,visited):
                    return True
        visited[x][y]=False
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word=="":
            return False
        visited=[[False for j in range(len(board[0]))] for i in range(len(board))]
        index=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[index]==board[i][j]:
                    if self.find(board,word,i,j,index+1,visited):
                        return True
        return False
                    
