class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        station_count = len(gas)
        gaps = [None] * station_count
        
        for idx in range(station_count):
            gaps[idx] = gas[idx] - cost[idx]
            
        min_idx = 0
        min_val = 0
        total = 0
        
        for idx in range(station_count):
            total += gaps[idx]
            if min_val >= total:
                min_val, min_idx = total, idx
            
        if total < 0:
            return -1
        else:
            return (min_idx+1)%station_count