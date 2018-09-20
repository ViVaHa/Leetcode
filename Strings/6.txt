class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)==0:
            return ""
        if numRows==1 or len(s)<numRows:
            return s
        ans=["" for i in range(numRows)]
        count=0
        i=0
        while count<len(s):
            while count<len(s) and i<=numRows-1:
                ans[i]+=s[count]
                i+=1
                count+=1
            i-=2
            while count<len(s) and i>=1:
                ans[i]+=s[count]
                i-=1
                count+=1
        a=""
        for i in range(len(ans)):
            a+="".join(ans[i])
        return a
        
