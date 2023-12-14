with open('14.input') as f:
    board = [list(line) for line in f.readlines()]

def tiltNorth(input):
    board = input
    # for line on the board
    for ind, line in enumerate(board):
        if ind!=0:
            # for rock on the board
            for i,s in enumerate(line):
                if s == 'O':
                    # for all rows above
                    for j in [x for x in range(ind)][::-1]:
                        if board[j][i] == '.':
                            board[j][i] = 'O'
                            board[j+1][i] = '.'
                        else: 
                            break
    return board

def count(board):
    count = 0
    for i, line in enumerate(tiltNorth(board)):
        count += (len(board) - i)* line.count('O')
    return count

print("count", count(board))


