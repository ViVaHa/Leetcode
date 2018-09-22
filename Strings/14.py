class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        i=0
        while i<(min(len(strs[0]),len(strs[1]))):
            if strs[1][i]!=strs[0][i]:
                break
            i+=1
        if i==0:
            return ""
        common=strs[0][0:i+1]
        for string in strs:
            while i<(len(common)) and i<len(string):
                if common[i]!=string[i]:
                    break
                i+=1
            if i!=len(common):
                common=common[0:i]
            i=0
        return common
            
        
