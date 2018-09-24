class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0
        if len(coins)==0:
            return -1
        coins.sort()
        dp=[amount+1 for i in range(amount+1)]
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if i>=coin:
                    dp[i]=min(dp[i],dp[i-coin]+1)
        if dp[-1]>amount:
            return -1
        else:
            return dp[-1]
        
                
                    
        
