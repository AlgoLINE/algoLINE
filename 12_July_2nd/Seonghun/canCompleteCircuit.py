class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        
        length = len(gas)
        sumVal = 0
        minIdx = 0
        minSum = sys.maxint 
        
        # accumulate the diff between gas and cost at each station
        for i in range(0, length):
            sumVal += (gas[i] - cost[i])
            if sumVal < minSum:     # update minimum accumulated diff between gas and cost
                minIdx = i
                minSum = sumVal
        
        if sumVal < 0:
            return -1
        else:
            idx = minIdx + 1        # since gas of the station at next index to minIdx is bigger than cost
            if idx < length:
                return idx
            else:
                return 0