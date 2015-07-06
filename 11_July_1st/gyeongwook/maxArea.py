class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        max_value = 0
        left_position = 0
        right_position = len(height)-1
        
        while left_position < right_position:
            max_value = max((right_position-left_position) * min(height[left_position], height[right_position]), max_value)
            
            if height[left_position] < height[right_position]:
                new_left = left_position+1
                while new_left < right_position and height[left_position] >= height[new_left]:
                    new_left += 1
                left_position = new_left
            else:
                new_right = right_position-1
                while new_right > left_position and height[right_position] >= height[new_right]:
                    new_right -= 1
                right_position = new_right
                
        return max_value