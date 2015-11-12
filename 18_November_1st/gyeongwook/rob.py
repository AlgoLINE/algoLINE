class Solution(object):
    def rob(self, nums):
        if nums is None: return 0
        
        length = len(nums)
        if length == 0: return 0
        
        lookup_table = []
        for column in range(length):
            lookup_table.append([0] * length)
        
        for segment_len in range(length):
            for start_idx in range(length-segment_len):
                end_idx = start_idx+segment_len
                
                if start_idx == end_idx:
                    lookup_table[start_idx][end_idx] = nums[start_idx]
                else:
                    for pivot in range(segment_len+1):
                        if pivot == 0:
                            lookup_table[start_idx][end_idx] = max(lookup_table[start_idx][end_idx], lookup_table[start_idx+1][end_idx])
                        elif pivot == segment_len:
                            lookup_table[start_idx][end_idx] = max(lookup_table[start_idx][end_idx], lookup_table[start_idx][end_idx-1])
                        else:
                            lookup_table[start_idx][end_idx] = max(lookup_table[start_idx][end_idx], lookup_table[start_idx][start_idx+pivot-1]+lookup_table[start_idx+pivot+1][end_idx])
                            
        return lookup_table[0][length-1]