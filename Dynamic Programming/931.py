class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if len(A)==0:
            return 0
        if len(A)==1:
            if len(A[0])==1:
                return A[0][0]
            else:
                return min(A[0])
            
        dp=[[0 for j in range(len(A[0]))] for i in range(len(A))]
        for i in range(len(A[0])):
            dp[0][i]=A[0][i]
        for i in range(1,len(A)):
            for j in range(len(A[i])):
                x,y,z=sys.maxsize,sys.maxsize,sys.maxsize
                if j-1>=0:
                    x=dp[i-1][j-1]
                y=dp[i-1][j]
                if j+1<len(A[i]):
                    z=dp[i-1][j+1]
                dp[i][j]=min(x,y,z)+A[i][j]
        minPath=sys.maxsize
        for j in range(len(A[0])):
            if minPath>dp[-1][j]:
                minPath=dp[-1][j]
        return minPath
            
