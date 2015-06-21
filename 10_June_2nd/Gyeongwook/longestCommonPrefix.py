class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
            
        common_prefix = strs[0]
        
        for each_str in strs:
            for idx in range(len(common_prefix)):
                if idx >= len(each_str) or each_str[idx] != common_prefix[idx]:
                    common_prefix = common_prefix[0:idx]
                    break;

        return common_prefix

        