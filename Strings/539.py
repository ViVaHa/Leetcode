class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timePoints.sort()
        prevTime=timePoints[-1]
        diff=sys.maxsize
        minVal=sys.maxsize
        ans=sys.maxsize
        for timePoint in timePoints:
            prevTimeStamp=int(prevTime.split(":")[0])*60+int(prevTime.split(":")[1])
            currTimeStamp=int(timePoint.split(":")[0])*60+int(timePoint.split(":")[1])
            if currTimeStamp-prevTimeStamp<0:
                diff=currTimeStamp-prevTimeStamp+1440
            else:
                diff=currTimeStamp-prevTimeStamp
            if diff<minVal:
                minVal=diff
            prevTime=timePoint
        return minVal
