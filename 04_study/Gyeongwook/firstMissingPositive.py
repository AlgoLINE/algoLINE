class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        arrayLen = len(A)
        
        for idx in range(0, arrayLen) :
            if A[idx] > 0 :
                if A[idx] > arrayLen :
                    A[idx] = -1
                elif A[idx] != idx + 1 :
                    tempIdx = A[idx]
                    A[idx] = -1
                    
                    while True :
                        if A[tempIdx - 1] == tempIdx or A[tempIdx - 1] < 1:
                            A[tempIdx - 1] = tempIdx
                            break
                        else :
                            temp = A[tempIdx - 1]
                            A[tempIdx - 1] = tempIdx
                            tempIdx = temp
                            
        for idx in range(0, arrayLen) :
            if A[idx] < 1 :
                return idx + 1
                
        return arrayLen + 1