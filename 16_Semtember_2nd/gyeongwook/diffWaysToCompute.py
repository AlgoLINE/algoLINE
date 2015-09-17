class Solution(object):
    def diffWaysToCompute(self, input):
        numbers = []
        operators = []
        
        current = ''
        for char in input:
            if char == '*' or char == '+' or char == '-':
                if current != '':
                    numbers.append(int(current))
                    current = ''
                operators.append(char)
            else:
                current += char
        numbers.append(int(current))
        
        number_count = len(numbers)
        lookup_table = [[[] for x in range(number_count)] for x in range(number_count)] 
        
        for segment_size in range(1, number_count+1):
            for start_idx in range(number_count-segment_size+1):
                if segment_size == 1:
                    lookup_table[start_idx][start_idx].append(numbers[start_idx])
                    continue
                    
                for pivot in range(1, segment_size):
                    for pre_part in lookup_table[start_idx][start_idx+pivot-1]:
                        for post_part in lookup_table[start_idx+pivot][start_idx+segment_size-1]:
                            if operators[start_idx+pivot-1] == '+':
                                lookup_table[start_idx][start_idx+segment_size-1].append(pre_part+post_part)
                            elif operators[start_idx+pivot-1] == '-':
                                lookup_table[start_idx][start_idx+segment_size-1].append(pre_part-post_part)
                            else:
                                lookup_table[start_idx][start_idx+segment_size-1].append(pre_part*post_part)
                
        return lookup_table[0][number_count-1]
        