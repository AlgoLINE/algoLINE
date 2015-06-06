class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        sequence = [0]
		
		for bitPos in range(n):
			count = 1 << bitPos
			for each in reversed(range(count)):
				sequence.append(sequence[each] + count)
				
		return sequence