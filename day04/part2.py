from helpers.read_lines import *
lines = read_input('day04')
"""
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?
"""
sample = read_sample_input('day04')

def create_boards(lines):
    boards = []
    board = []
    for line in lines:
        #signify end of board
        if line == '\n':
            boards.append(board)
            board = []
        else:
            row = []
            for number in line.strip().split(' '):
                #handle 2 spaces
                if number == '':
                    continue
                row.append(int(number))
            board.append(row)
    boards.append(board)
    return boards


def check_row(row):
    for number in row:
        if number != 'X':
            return False
    return True

def check_column(column):
    for number in column:
        if number != 'X':
            return False
    return True

def check_board(board):
    for row in board:
        if check_row(row):
            return True
    for column in zip(*board):
        if check_column(column):
            return True
    return False

def board_score(board):
    score = 0
    for row in board:
        for number in row:
            if number != 'X':
                score += number
    return score

def run():
    numbers = [int(x) for x in lines[0].split(',')]
    boards = create_boards(lines[2:])
    buffer = 0
    bail = False
    for number in numbers:
        if bail:
            break
        buffer += 1
        #find the number on the boards
        for board in boards:
            for row in board:
                if number in row:
                    #mark the number on the board
                    row[row.index(number)] = 'X'
        if buffer > 5:
            #check if any board has a complete row or column
            for board in boards:
                if check_board(board):
                    #remove the board unless it's the last one
                    if len(boards) == 1:
                        print(board_score(boards[0]) * number)
                        bail = True
                        break
                    boards.remove(board)
                else:
                    continue
