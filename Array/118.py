class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        ans=[]
        ans.append([1])
        for i in range(1,numRows):
            j=0
            temp=[]
            while j<=i:
                if j==0:
                    temp.append(ans[i-1][j])
                elif j==i:
                    temp.append(ans[i-1][j-1])
                else:
                    temp.append(ans[i-1][j-1]+ans[i-1][j])
                j+=1
            ans.append(temp)
        return ans
        
