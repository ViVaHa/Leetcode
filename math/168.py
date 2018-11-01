class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==0:
            return -1
        string=""
        while n>=1:
            rem=n%26
            if rem==0:
                rem=26
                n=int(n/26)-1
            else:
                n=int(n/26)
            string=str(chr(int(rem)+64))+string
            
        return string
            
