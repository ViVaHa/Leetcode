class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s=="":
            return 0
        if len(s)==1:
            if s=='0':
                return 0
            return 1
        dp=[0 for i in range(len(s)+1)]
        dp[0]=1
        for i in range(1,len(s)+1):
            if s[i-1]!='0':
                dp[i]+=dp[i-1]
            if i!=1 and s[i-2:i]<'27' and s[i-2:i]>'09':
                dp[i]+=dp[i-2]
        return dp[len(s)]
        
