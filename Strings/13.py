class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        d={}
        d['M']=1000
        d['D']=500
        d['C']=100
        d['L']=50
        d['X']=10
        d['V']=5
        d['I']=1
        n=len(s)-2
        count=d.get(s[n+1])
        while n>=0:
            if d.get(s[n])>=d.get(s[n+1]):
                count+=d.get(s[n])
            else:
                count-=d.get(s[n])
            n-=1
        return count
                
                
        
        
        
