class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote=="":
            return True
        if magazine=="":
            return False
        i=0
        idx=0
        d={}
        for i in range(len(magazine)):
            if magazine[i] in d:
                d[magazine[i]]+=1
            else:
                d[magazine[i]]=1
        for i in range(len(ransomNote)):
            if ransomNote[i] not in d or d[ransomNote[i]]==0:
                return False
            else:
                d[ransomNote[i]]-=1
        return True
