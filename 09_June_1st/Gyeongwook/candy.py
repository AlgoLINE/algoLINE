class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        candy = 0
        current_candy = 1
        
        section_info = []
        section_len = 1
        
        for each in range(1, len(ratings)):
            section_len += 1
            
            gap = ratings[each-1] - ratings[each]
            if gap < 0:
                current_candy += 1
            else:
                section_info.append((section_len-1, current_candy))
                
                if gap == 0:
                    candy += self.flush(section_info)
                	
                current_candy = 1
                section_len = 1
        
        section_info.append((section_len, current_candy))
        candy += self.flush(section_info)
        
        return candy
    	
    def flush(self, section_info):
        candy_sum = 0
        
        section_len = 0
        last_candy = 0
        before_candy = 0
        
        while len(section_info) > 0:
            (section_len, last_candy) = section_info.pop()
            candy_sum += (section_len * (section_len+1) / 2)
            
            if last_candy <= before_candy:
                candy_sum += (before_candy - last_candy + 1)
            	
            before_candy = 1 if section_len > 1 else before_candy+1

        return candy_sum