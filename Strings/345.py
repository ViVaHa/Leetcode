class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return s
        d={}
        d['a']=1
        d['e']=1
        d['i']=1
        d['o']=1
        d['u']=1
        d['A']=1
        d['E']=1
        d['I']=1
        d['O']=1
        d['U']=1
        a=list(s)
        left=0
        right=len(s)-1
        while left<=right:
            if a[left] not in d:
                left+=1
            elif a[right] not in d:
                right-=1
            else:
                swap=a[left]
                a[left]=a[right]
                a[right]=swap
                left+=1
                right-=1
        return "".join(a)
        
