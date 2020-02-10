
# board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for row in board:
#     for column in row:
#         if column == row[-1]:
#             print(column)
#         else:
#             print(column, end=" ")


# def gen_board(size=3, value=0):
#     for i in range(size):
#         row = []
#         for j in range(size):
#             row.append(0)
#         board.append(row)
#     return board
#
#
# print(gen_board(4))

size = 3

# board = [[0]*size for i in range(size)]

# board = [[0 for i in range(size)] for j in range(size)]

# board = [[i+1+(j*size) for i in range(size)] for j in range(size)]

# board = []
# for i in range(size):
#     row = []
#     for j in range(size):
#         row.append(j+1+(i*size))
#     board.append(row)

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

board[len(board)//2][len(board)//2] = 3

print(board)
