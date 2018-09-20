class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        l=-1
        prevL=False
        countA=0
        for i in range(len(s)):
            if s[i]=='A':
                countA+=1
                if countA>1:
                    return False
            if s[i]=='L':
                #print(prevL,l)
                if prevL and l!=-1:
                    if i-l>=2:
                        return False
                else:
                    if not(prevL):
                        prevL=True
                        l=i
            else:
                prevL=False
                l=-1
        return True
