class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        start=0
        i=0
        size=0
        while i<len(s) and s[i]==" ":
            i+=1
        start=i
        while i<len(s):
            if s[i]==" ":
                size=i-start  
                while i<len(s) and s[i]==" ":
                    i+=1
                start=i
            if i<len(s):
                i+=1
        if s[i-1]!=" ":
            size=i-start
        return size
