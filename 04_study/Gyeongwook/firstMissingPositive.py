class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        arrayLen = len(A)
        
        for idx in range(0, arrayLen) :
            if A[idx] < 1 :
                continue

            temp = A[idx]
            A[idx] = -1

            if temp <= arrayLen :
                self.sort(A, temp)
                            
        for idx in range(0, arrayLen) :
            if A[idx] < 1 :
                return idx + 1
                
        return arrayLen + 1

    def sort(self, A, startIdx):
        currentIdx = startIdx

        while True :
            if A[currentIdx - 1] != currentIdx and A[currentIdx - 1] > 0 :
                temp = A[currentIdx - 1]
                A[currentIdx - 1] = currentIdx
                currentIdx = temp
            else :
                A[currentIdx - 1] = currentIdx
                return
