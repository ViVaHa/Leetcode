class Solution:
    def formCoordinates(self,S,arr):
        n=len(S)
        if n==0 or (n>1 and S[n-1]=='0' and S[0]=='0'):
            return
        elif n>1 and (S[0]=='0'):
            arr.append("0."+S[1:])
            return
        arr.append(S)
        if n==1 or S[n-1]=='0':
            return
        for i in range(len(S)-1):
            arr.append(S[0:i+1]+"."+S[i+1:])
            
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if len(S)==0:
            return 0
        S=S[1:len(S)-1]
        ones=[]
        twos=[]
        ans=[]
        for i in range(len(S)):
            one=S[0:i+1]
            two=S[i+1:len(S)]
            self.formCoordinates(one,ones)
            self.formCoordinates(two,twos)
            for o in ones:
                for t in twos:
                    ans.append("("+o+", "+t+")")
            ones=[]
            twos=[]
        
        return ans
            
            
        
