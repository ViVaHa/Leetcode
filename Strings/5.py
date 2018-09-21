class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return ""
        n=len(s)
        dp=[[False for j in range(len(s))] for i in range(len(s))]
        x=0
        y=0
        maxlen=0
        for i in range(len(s)):
            dp[i][i]=True
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                if maxlen<2:
                    x=i
                    y=i+1
                    maxlen=2
        length=2
        while length<n:
            i=0
            j=i+length
            while j<n:
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]
                    if maxlen<j-i+1 and dp[i][j]:
                        maxlen=j-i+1
                        x=i
                        y=j
                i+=1
                j+=1
            length+=1
        return s[x:y+1]
