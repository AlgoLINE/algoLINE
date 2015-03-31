class Solution:
    # @return a string
    def convertToTitle(self, num):
        resultNumbers = []
        baseChar = ord('A')

        returnValue = ''
        srcNumber = num

        while True :
            srcNumber = srcNumber - 1
            returnValue = chr(srcNumber % 26 + baseChar) + returnValue
            srcNumber = srcNumber / 26
            
            if srcNumber is 0 :
                break

        return returnValue