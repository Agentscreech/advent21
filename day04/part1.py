from helpers.read_lines import *
lines = read_input('day04')
"""
Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?
"""
sample = read_sample_input('day04')

def create_boards(sample):
    boards = ()
    board = []
    for line in sample:
        #signify end of board
        if line == '\n':
            boards += (board,)
            board = []
        else:
            row = []
            for number in line.strip().split(' '):
                #handle 2 spaces
                if number == '':
                    continue
                row.append(int(number))
            board.append(row)
    boards += (board,)
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
                    #calculate the score
                    print(number * board_score(board))
                    bail = True
                else:
                    continue



    