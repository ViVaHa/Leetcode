class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)==0 and len(b)==0:
            return ""
        elif len(a)==0:
            return b
        elif len(b)==0:
            return a
        diff=abs(len(a)-len(b))
        if len(a)<len(b):
            while diff>0:
                a='0'+a
                diff-=1
        else:
            while diff>0:
                b='0'+b
                diff-=1
        num1=list(a)
        num2=list(b)
        ans=[]
        carry=0
        for i in range(len(num1)-1,-1,-1):
            num=int(num1[i])+int(num2[i])+carry
            carry=int(num/2)
            num=num%2
            ans.insert(0,str(num))
        if carry>0:
            ans.insert(0,str(carry))
        return "".join(ans)
    
            `
