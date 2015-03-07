class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        returnVal = 0;

        for each in A:
            returnVal = returnVal ^ each

        return returnVal