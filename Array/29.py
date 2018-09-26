class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend==0:
            return 0
        positive=False
        if (dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            positive=True
        dividend,divisor=abs(dividend),abs(divisor)
        temp=divisor
        ans=0
        rem=dividend
        while rem>=divisor:
            temp=divisor
            multiple=1
            dividend=rem
            while dividend>(temp<<1):
                temp=temp<<1
                multiple=multiple<<1
            ans+=multiple
            rem-=temp
        if positive:
            return min(ans,2147483647)
        else:
            return max(-ans,-2147483648)
