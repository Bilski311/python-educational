# How tic tac toe can go wrong
# Correct:
correct_board = [['_'] * 3 for _ in range(3)]
correct_board[2][1] = 'X'
for row in correct_board:
    print(row)

print('=====================')
weird_board = [['_'] * 3] * 3
weird_board[2][1] = 'X'
for row in weird_board:
    print(row)
