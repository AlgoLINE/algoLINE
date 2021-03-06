class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
        row_len = len(dungeon)
        col_len = len(dungeon[0])
		
        cost_lookup_table = {}
        dungeon_depth = row_len + col_len
		
        for depth in range(dungeon_depth-1) :
            col_idx = depth if depth < col_len else col_len - 1
			
            while col_idx >= 0 :
                row_idx = depth - col_idx
                
                if row_idx > row_len :
                    break
                
                actual_row_idx = row_len - row_idx - 1
                actual_col_idx = col_len - col_idx - 1
                
                cost_lookup_table[(actual_row_idx, actual_col_idx)] = self.get_optimal_path(actual_row_idx, actual_col_idx, row_len, col_len, dungeon, cost_lookup_table)
                
                col_idx -= 1
				
        current_hp = 0
        minimum_hp = 0
        current_tile = (0, 0)
        
        for step in range(dungeon_depth-1) :
            current_hp += dungeon[current_tile[0]][current_tile[1]]
            minimum_hp = min(minimum_hp, current_hp)
            
            current_tile = cost_lookup_table[current_tile][1]
				
        minimum_hp = -minimum_hp + 1
        return minimum_hp if minimum_hp > 0 else 0	
		
    def get_optimal_path(self, row_idx, col_idx, row_len, col_len, dungeon, lookup_table):
        minimum_hp = dungeon[row_idx][col_idx]
        next_coordinate = None
        
        right_tile = None
        below_tile = None
        
        right_value = None
        below_value = None
        
        if col_idx < col_len-1 :
            right_tile = (row_idx, col_idx+1)
            right_value = lookup_table[right_tile][0]
		
        if row_idx < row_len-1 :        
            below_tile = (row_idx+1, col_idx)
            below_value = lookup_table[below_tile][0]
	
        if right_tile is None and below_tile is None :
            minimum_hp = dungeon[row_idx][col_idx] if dungeon[row_idx][col_idx] < 0 else 0
        elif right_tile is not None and below_tile is not None :
            next_coordinate = right_tile if right_value > below_value else below_tile
            optimal_path_hp = max(right_value, below_value) 
            minimum_hp = dungeon[row_idx][col_idx] + optimal_path_hp if dungeon[row_idx][col_idx] + optimal_path_hp < 0 else 0
        elif right_tile is not None :
            minimum_hp = dungeon[row_idx][col_idx] + lookup_table[right_tile][0] if dungeon[row_idx][col_idx] + lookup_table[right_tile][0] < 0 else 0
            next_coordinate = right_tile
        else :
            minimum_hp = dungeon[row_idx][col_idx] + lookup_table[below_tile][0] if dungeon[row_idx][col_idx] + lookup_table[below_tile][0] < 0 else 0
            next_coordinate = below_tile
		
        return (minimum_hp, next_coordinate)