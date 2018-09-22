class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)==0 and len(haystack)==0:
            return 0
        if len(needle)==len(haystack):
            if needle==haystack:
                return 0
            else:
                return -1
        l=len(needle)
        for i in range(len(haystack)-len(needle)+1):
            #print(haystack[i:i+l])
            if haystack[i:i+l]==needle:
                return i
        return -1
