class Solution(object):
    def groupAnagrams(self, strs):
        table = {}
        
        for each_str in strs:
            key = ''.join(sorted(each_str))
            if key in table:
                table[key].append(each_str)
            else:
                table[key] = [each_str]
                
        result = []
        for value in table.values():
            result.append(sorted(value))
            
        return result