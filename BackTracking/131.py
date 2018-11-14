import copy
class Solution:
    def partitionPalindromes(self,s,dp,ans,temp,index):
        if index==len(s):
            ans.append(copy.deepcopy(temp))
            return
        for i in range(index,len(s)):
            if dp[index][i]:
                temp.append(s[index:i+1])
                self.partitionPalindromes(s,dp,ans,temp,i+1)
                temp.pop()
        
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s)==0:
            return 0
        dp=[[False for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i]=True
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
        for l in range(2,len(s)):
            for i in range(len(s)-l):
                j=i+l
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
        temp=[]
        ans=[]
        self.partitionPalindromes(s,dp,ans,temp,0)
        return ans
            
        
