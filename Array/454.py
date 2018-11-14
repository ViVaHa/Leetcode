class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        d={}
        count=0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i]+B[j] in d:
                    d[A[i]+B[j]]+=1
                else:
                    d[A[i]+B[j]]=1
        for i in range(len(C)):
            for j in range(len(D)):
                val=C[i]+D[j]
                if -val in d:
                    count+=d[-val]
        return count
        
