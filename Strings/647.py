class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0 or len(s)==1:
            return len(s)
        length=len(s)
        dp=[[0 for i in range(len(s))] for j in range(len(s))]
        i=0
        res=0
        for i in range(len(s)):
            dp[i][i]=1
            res+=1
        size=1
        while size<length:
            i=0
            j=i+size
            while i+size<length:
                if s[i]==s[j]:
                    if i+1<=j-1:
                        if dp[i+1][j-1]:
                            res+=1
                            dp[i][j]=1
                    else:
                        res+=1
                        dp[i][j]=1
                i+=1
                j=i+size
            size+=1
        return res
        
