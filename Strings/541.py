class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k==0:
            return s
        l=list(s)
        if len(s)==0:
            return ""
        for i in range(0,len(s),2*k):
            l[i:i+k]=reversed(l[i:i+k])
        
        return "".join(l)
                
        
