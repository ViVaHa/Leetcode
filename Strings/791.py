class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        if len(S)==0:
            return ""
        d={}
        r={}
        for i in range(len(S)):
            d[S[i]]=i
            r[i]=S[i]
        l=[]
        count=500
        for i in range(len(T)):
            if T[i] in d:
                l.append(d[T[i]])
            else:
                l.append(count)
                r[count]=T[i]
                d[T[i]]=count
                count-=1
        l.sort()
        ans=""
        for i in range(len(l)):
            ans+=(r[l[i]])
        #print(d,r)
        return (ans)
            
        
