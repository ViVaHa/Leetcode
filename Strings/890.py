class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        if len(pattern)==0:
            return None
        ans=[]
        d={}
        count=1
        add=True
        for word in words:
            d={}
            r={}
            add=True
            for i in range(len(pattern)):
                if (pattern[i] not in d or word[i] not in r):
                    if pattern[i] not in d:
                        d[pattern[i]]=word[i]
                    if word[i] not in r:
                        r[word[i]]=pattern[i]
                if d[pattern[i]]!=word[i] or r[word[i]]!=pattern[i]:
                    add=False
                    break
            if add:
                ans.append(word)
        return ans
            
