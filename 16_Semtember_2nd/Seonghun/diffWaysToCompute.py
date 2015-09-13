class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        self.results = [];
        
        prvIdx = 0
        vs = []             # operands
        ops = []            # operators
        for idx in xrange(0,len(input)):            # divide each operand and operator
            if input[idx] == '+' or input[idx] == '-' or input[idx] == '*':
                ops.append(input[idx])
                vs.append(int(input[prvIdx:idx]))
                prvIdx = idx+1
        vs.append(int(input[prvIdx:]))
        
        self.compute(0, vs, ops)
        return self.results;
        
    def compute(self, startIdx, vs, ops):           # compute recursively. It will cost O(n^2) space complexity
        size = len(vs)
        if size == 1:
            self.results.append(vs[0])
            return
        for idx in xrange(startIdx, size-1):
            newV = self.cal(vs[idx], vs[idx+1], ops[idx])
            newVs = vs[:idx] + [newV] + vs[idx+2:]
            newOps = ops[:idx] + ops[idx+1:]
            newSIdx = idx-1                         # key ponints for removing redundant computations.
            if newSIdx < 0:
                newSIdx = 0
            self.compute(newSIdx, newVs, newOps)
        
    def cal(self, v1, v2, op):
        if op == '+':
            return v1 + v2
        if op == '-':
            return v1 - v2
        if op == '*':
            return v1 * v2
        return 0