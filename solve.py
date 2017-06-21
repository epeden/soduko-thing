from board import Board


class Solver:

	def __init__(self,cells='abc',steps=None,random_solve=False,test=False):

		self.cells = cells
		self.nums = [str(i) for i in range(1,10)]
		self.build_board()
		print('\n*************************************')
		print('****** SolveDoku Sudoku Solver ******')
		print('*************************************\n')
		print('     Here is your puzzle:')
		self.board.print_board()		

	def build_board(self):
		self.board = Board(self.cells)
		self.orig_board = Board(self.cells)

	def solve(self):
		cells_enum = list(enumerate(self.cells))
		solved = False
		count = 0
		while solved == False:
			count = count + 1

			for num in self.nums:
				for row in self.board.rows:
					fit = []
					for cell in row:
						if cell.value == '0':
							recv = self.check_cell(num,cell)
							if recv == cell:
								fit.append(recv)
					if len(fit) == 1:
						self.board.set_cell(str(num), fit[0].index)
				for column in self.board.columns:
					fit = []
					for cell in column:
						if cell.value == '0':
							recv = self.check_cell(num,cell)
							if recv == cell:
								fit.append(recv)
					if len(fit) == 1:
						self.board.set_cell(str(num), fit[0].index)
				for block in self.board.blocks:
					fit = []
					for cell in block:
						if cell.value == '0':
							recv = self.check_cell(num,cell)
							if recv == cell:
								fit.append(recv)
					if len(fit) == 1:
						self.board.set_cell(str(num), fit[0].index)

			# check if board solved
			if not '0' in self.board.cell_list:
				solved = True
				self.print_solution()
				return

			# cutoff, not gonna solve
			if count == 5000:
				if self.board.cell_list == self.orig_board.cell_list:
					print("Board didn't change!!")
					return
				else:
					print('Could not solve in {} cycles...'.format(str(count)))
					self.board.print_board()
					return
		return

	def check_cell(self,num,cell):
		check = []
		check.append(self.search_row(num,cell))
		check.append(self.search_column(num,cell))
		check.append(self.search_block(num,cell))
		if False not in check:
			return cell
		return False
	
	def search_row(self,num,cell):
		for c in self.board.rows[cell.row]:
			if c.value == num:
				return False
		return cell

	def search_column(self,num,cell):
		for c in self.board.columns[cell.column]:
			if c.value == num:
				return False
		return cell

	def search_block(self,num,cell):
		for c in self.board.blocks[cell.block]:
			if c.value == num:
				return False
		return cell

	def print_solution(self):
		print('\n    Here is the solution:')
		self.board.print_board()
		print('')

	def print_groups(self):
		for r in self.board.rows:
			print('row: {}'.format(''.join(str(c.value) for c in r)))
		for r in self.board.columns:
			print('column: {}'.format(''.join(str(c.value) for c in r)))
		for r in self.board.blocks:
			print('block: {}'.format(''.join(str(c.value) for c in r)))


