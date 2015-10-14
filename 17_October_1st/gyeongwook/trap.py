class Solution(object):
    def trap(self, height):
		left_height = []
        right_heights = []
		
		max_height = 0
		for each in height:
			left_height.append(max_height)
			max_height = max(max_height, each)
			
		max_height = 0
		for each in reversed(height):
			right_heights.append(max_height)
			max_height = max(max_height, each)
		right_heights.reverse()
		
		traped = 0
		for idx in range(len(height)):
			each_traped = min(left_height[idx], right_heights[idx]) - height[idx]
			traped += each_traped if each_traped > 0 else 0
		
		return traped