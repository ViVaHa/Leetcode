class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        res=0
        for i in range(len(s)):
            val=ord(s[i])-64
            res*=26
            res+=val
        return res
