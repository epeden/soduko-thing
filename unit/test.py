import sys
import board
import solve



TEST_BOARD = '072069500300020860000000790950004100740600000000008940680500001020041007000080000'



solver = Solver(TEST_BOARD)

print('Running unit tests...')
assert(solver.build_board())



print('All unit tests passed')