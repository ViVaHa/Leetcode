class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        for i in range(len(s)):
            if ord(s[i]) in range(65,92):
                l.append(s[i].lower())
            elif ord(s[i]) in range(97,124):
                l.append(s[i])
            elif ord(s[i]) in range(48,58):
                l.append(s[i])
        if "".join(l)=="".join(reversed(l)):
            return True
        else:
            return False
        
