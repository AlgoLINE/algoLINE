class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
            
        lookup_table = [
            [' '],	                # 0
            [],	                    # 1
            ['a', 'b', 'c'],        # 2
            ['d', 'e', 'f'],        # 3
            ['g', 'h', 'i'],        # 4
            ['j', 'k', 'l'],        # 5
            ['m', 'n', 'o'],        # 6
            ['p', 'q', 'r', 's'],   # 7
            ['t', 'u', 'v'],        # 8
            ['w', 'x', 'y', 'z']    # 9
        ]
        
        result = ['']
        for each_digit in digits:
            digit = int(each_digit)
            new_result = []
            element_number = len(result)
            
            for each_result in result:
                for each_char in lookup_table[digit]:
                    new_result.append(each_result + each_char)
            
            result = new_result
        
        return result