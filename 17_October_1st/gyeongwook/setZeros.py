class Solution(object):
    def setZeroes(self, matrix):
		lookup_table_row = set()
		lookup_table_column = set()
		
		for idx_row, each_row in enumerate(matrix):
			for idx_column, each_element in enumerate(each_row):
				if each_element == 0:
					lookup_table_row.add(idx_row)
					lookup_table_column.add(idx_column)
					
		for idx_row in range(len(matrix)):
			for idx_column in range(len(matrix[0])):
				if idx_row in lookup_table_row or idx_column in lookup_table_column:
					matrix[idx_row][idx_column] = 0