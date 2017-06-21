from collections import defaultdict

class Cell:

	def __init__(self,index, value, column, row, block):
		self.index = index
		self.value = value
		self.column = column
		self.row = row
		self.block = block


class Board:
	
	def __init__(self,new_cells):

		self.cell_list = new_cells
		self.new_cells = list(enumerate(new_cells))
		self.cells = []
		assert (len(self.cell_list) == 81
				), ('Wrong number of cells for board: {}, need 81.'.format(len(self.cell_list)))			

		for c in self.new_cells:
			index = self.new_cells.index(c)
			cell_column = int(index) % 9 
			cell_row = int(index/9)
			cell_block = self.find_block(cell_column, cell_row)
			cell = Cell(index,self.cell_list[index], cell_column, cell_row, cell_block)
			self.cells.append(cell)

		self.blocks = self.build_blocks_from_cells(self.cells)
		self.rows = self.build_rows_from_cells(self.cells)
		self.columns = self.build_columns_from_cells(self.cells)
	
	def build_blocks_from_cells(self,cells):
		blocks = []
		for i in range(9):
			block = []
			for c in cells:
				if c.block == i:
					block.append(c)
			blocks.append(block)
		return blocks

	def build_rows_from_cells(self,cells):
		rows = []
		for i in range(0,80,9):
			row = []
			this_row = cells[i:i+9]
			for r in this_row:
				row.append(r)
			rows.append(row)
		return rows

	def build_columns_from_cells(self,cells):
		columns = []
		for i in range(9):
			column = []
			this_column = cells[i::9]
			for c in this_column:
				column.append(c)
			columns.append(column)
		return columns

	def set_cell(self, value, index):
		self.cells[index].value = value
		self.cell_list = self.cell_list[:index] + value + self.cell_list[index+1:]


	def find_block(self, col, row):
		x = int((row) / 3)
		y = int((col) / 3)
		l = []
		l.append([0,1,2])
		l.append([3,4,5])
		l.append([6,7,8])
		return l[x][y]

	def print_board(self):
		s = ''
		s += '-----------------------------'
		for i in range(0,len(self.cells)):
			if i == 27 or i == 54:
				s += '\n---------+---------+---------'
			if i % 9 == 3 or i % 9 == 6:
				s += '|'
			if i % 9 == 0:
				s += '\n'
			s += ' {} '.format(self.cells[i].value if self.cells[i].value != '0' else ' ')
		print(s + '\n-----------------------------')






