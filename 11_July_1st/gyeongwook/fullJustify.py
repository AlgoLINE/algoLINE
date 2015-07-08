class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        return_container = []
        
        temp_container = []
        current_len = 0
        
        for each_word in words:
            if current_len + len(temp_container) + len(each_word) > maxWidth:
                return_container.append(self.flush(temp_container, current_len, maxWidth))
                current_len = 0
                temp_container[:] = []
                
            current_len += len(each_word)
            temp_container.append(each_word)
            
        last_part = ""
        for each in temp_container:
            last_part += (each + " ")
            
        if len(last_part) < maxWidth:
            last_part += (" " * (maxWidth-len(last_part)))
            
        return_container.append(last_part[:maxWidth])
            
        return return_container
        
    def flush(self, temp_container, current_len, maxWidth):
        margin = maxWidth - current_len
        base = " " * (margin / max(1, (len(temp_container)-1)))
        rest = margin % max(1, (len(temp_container)-1))
        
        current_str = ""
        for each in temp_container:
            current_str += (each + base)
            if rest > 0:
                current_str += " "
                rest -= 1
                
        return current_str[:maxWidth]