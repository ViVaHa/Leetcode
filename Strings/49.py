class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs)==0:
            return None
        d={}
        for i in range(len(strs)):
            key=''.join(sorted(strs[i]))
            if not(key in d):
                d[key]=[]
            d[key].append(strs[i])
        ans=[]
        inner=[]
        for k in d:
            ans.append(d[k])
        return ans
        
