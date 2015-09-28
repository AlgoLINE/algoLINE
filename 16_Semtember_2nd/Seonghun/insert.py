# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        
        result = []
        phase = 0   # 0 is finding start position, 1 is finding end position, 2 is done.
        start = 0
        end = 0
        for interval in intervals: 
            addCurrentInterval = True
            if phase == 0:
                if newInterval.end < interval.start:
                    start = newInterval.start
                    phase = 1
                else:
                    if newInterval.start < interval.start:
                        start = newInterval.start
                        phase = 1
                    elif newInterval.start <= interval.end:
                        start = interval.start
                        phase = 1
            
            if phase == 1:
                if newInterval.end < interval.start:
                    end = newInterval.end
                    phase = 2
                    result.append(Interval(start, end))
                elif newInterval.end <= interval.end:
                    end = interval.end
                    phase = 2
                    addCurrentInterval = False
                    result.append(Interval(start, end))
            
            if phase == 0:
                result.append(interval)
            elif phase == 2 and addCurrentInterval:
                result.append(interval)
        
        if phase == 0:
            result.append(newInterval)        
        if phase == 1:
            result.append(Interval(start, newInterval.end))
        
        return result