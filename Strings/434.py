class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        count=0
        i=0
        while i<len(s) and s[i]==" ":
            i+=1
        while i < (len(s)):
            if s[i]==" ":
                while i<len(s) and s[i]==" ":
                    i+=1
                count+=1 
            if i<len(s):
                i+=1
        if s[i-1]!=" ":
            count+=1
        return count
