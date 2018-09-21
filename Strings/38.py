class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==0:
            return 0
        if n==1:
            prev="1"
            return prev
        elif n==2:
            prev="11"
            return prev
        i=0
        ans=""
        prev="11"
        while n-2>0:
            n-=1
            i=0
            curr=0
            count=1
            while i<len(prev):
                while i<len(prev)-1 and prev[i]==prev[i+1]:
                    count+=1
                    i+=1
                ans+=str(count)+str(prev[curr])
                count=1
                curr=i+1
                i+=1
            prev=ans
            ans=""
        return prev
        
                    
                
            
        
