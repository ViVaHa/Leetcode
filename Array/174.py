class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if len(dungeon)==0 or len(dungeon[0])==0:
            return 0
        if len(dungeon)==1 and len(dungeon[0])==1:
            if dungeon[0][0]<=0:
                return -dungeon[0][0]+1
            else:
                return 1
        dp=[[0 for j in range(len(dungeon[0]))] for i in range(len(dungeon))]
        columns=len(dungeon[0])-1
        rows=len(dungeon)-1
        if dungeon[-1][-1]<=0:
            dp[-1][-1]=-dungeon[-1][-1]+1
        else:
            dp[-1][-1]=1
        for i in range(rows-1,-1,-1):
            dp[i][columns]=max(dp[i+1][columns]-dungeon[i][columns],1)
        for j in range(columns-1,-1,-1):
            dp[rows][j]=max(dp[rows][j+1]-dungeon[rows][j],1)
        for i in range(rows-1,-1,-1):
            for j in range(columns-1,-1,-1):
                if dp[i+1][j]<=0:
                    x=1
                else:
                    x=dp[i+1][j]
                if dp[i][j+1]<=0:
                    y=1
                else:
                    y=dp[i][j+1]
                dp[i][j]=min(x,y)-dungeon[i][j]
        #print(dp)
        return max(1,dp[0][0])
        
