class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        d={}
        maxVal=0
        start=0
        i=0
        if len(s)==1:
            return 1
        i=0
        j=0
        while i<(len(s)) and j<len(s):
            if not(s[j] in d):
                d[s[j]]=j
                if j-i+1>maxVal:
                    maxVal=j-i+1
                j+=1
            else:
                del d[s[i]]
                i+=1
                
        
        return maxVal
