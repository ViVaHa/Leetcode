class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d={}
        for x in s:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        for y in t:
            if y in d:
                d[y]-=1
            else:
                return False
        for k,v in d.items():
            if v!=0:
                return False
        return True
