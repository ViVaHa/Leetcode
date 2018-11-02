class Solution:
    def compute(self,num):
        ans=0
        while num>0:
            rem=num%10
            ans=ans+(rem**2)
            num=int(num/10)
        return ans
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        if n==1:
            return True
        slow=self.compute(n)
        fast=self.compute(n)
        fast=self.compute(fast)
        while slow!=fast:
            if slow==1:
                return True
            slow=self.compute(slow)
            fast=self.compute(fast)
            fast=self.compute(fast)
        if fast==1:
            return True
        else:
            return False
        
