class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        currentSeq = "1"
        
        for each in range(n-1) :
            newStr = ""
            
            currentNumber = int(currentSeq[0])
            currentLen =  len(currentSeq)
            currentCount = 0
            
            for idx in range(currentLen) :
                currentCount += 1
                if idx >= currentLen-1 or currentSeq[idx] != currentSeq[idx+1] :
                    newStr += str(currentCount)
                    newStr += currentSeq[idx]
                    currentCount = 0
            		
            currentSeq = newStr
            
        return currentSeq