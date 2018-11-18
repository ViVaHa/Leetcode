class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        x=0
        for num in nums:
            if len(str(num))>x:
                x=len(str(num))
        l=[]
        d={}
        x+=1
        for num in nums:
            s=str(num)*x
            if s[:x:] in d:
                d[s[:x:]].append(str(num))
            else:
                d[s[:x:]]=[]
                d[s[:x:]].append(str(num))
            l.append(s[:x:])
        l=set(l)
        l=sorted(l,reverse=True)
        
        if d[l[0]][0]=="0":
            return "0"
        ret=""
        
        for item in l:
            list=d[item]
            for h in list:
                #print(h)
                ret+=h
        return ret
        
        
            
            
        
