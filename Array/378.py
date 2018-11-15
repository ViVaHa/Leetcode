class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        l=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                l.append(matrix[i][j])
        heapq.heapify(l)
        x=0
        while k>0:
            x=heapq.heappop(l)
            k-=1
        return x
            
        
        
