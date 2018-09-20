class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        groups=[1]
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                groups.append(1)
            else:
                groups[-1]+=1
        count=0
       # print(groups)
        for i in range(1,len(groups)):
            count+=min(groups[i],groups[i-1])
        return count
            
