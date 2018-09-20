class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return -1
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1
