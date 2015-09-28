# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
		merged_interval = []
		inserted = False
		
		for each_interval in intervals:
			if each_interval.end < newInterval.start:
				merged_interval.append(each_interval)
			else:
				if not inserted:
					inserted = True
					merged_interval.append(newInterval)
				
				if newInterval.end < each_interval.start:
					merged_interval.append(each_interval)
				else:
					newInterval.start = min(each_interval.start, newInterval.start)
					newInterval.end = max(each_interval.end, newInterval.end)
					
		if not inserted:
			merged_interval.append(newInterval)
			
		return merged_interval