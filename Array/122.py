class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        buy=prices[0]
        i=1
        profit=0
        n=len(prices)
        while i<n:
            while i<n and prices[i]<prices[i-1]:
                i+=1
            buy=prices[i-1]
            while i<n-1 and prices[i]<prices[i+1]:
                i+=1
            if i<n:
                sell=prices[i]
                profit+=sell-buy
            i+=1
        return profit
        
