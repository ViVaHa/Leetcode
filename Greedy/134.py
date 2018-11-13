class Solution:
    def canCompleteCircuit(self, gas, cost):
        
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas)==1:
            if gas[0]-cost[0]>=0:
                return 0
            return -1
        if len(gas)==0:
            return -1
        start=0
        end=1
        rem=gas[start]-cost[start]
        l=len(gas)
        while start!=end or rem<0:
            while rem<0 and end!=start:
                rem-=gas[start]-cost[start]
                start=(start+1)%l
                if start==0:
                    return -1
            rem+=gas[end]-cost[end]
            end=(end+1)%l
        return start
                
            
