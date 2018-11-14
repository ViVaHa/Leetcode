# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)==0:
            return []
        intervals.sort(key=lambda x:x.start)
        ans=[]
        ans.append(intervals[0])
        append=False
        for interval in intervals:
            if ans[-1].end>=interval.start:
                ans[-1].end=max(ans[-1].end,interval.end)
            else:    
                ans.append(interval)
        return ans
