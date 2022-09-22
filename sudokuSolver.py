board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# Recursive backtracking
def solve(bo):
    # basecase: board is filled up
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10): # loop through 1-9
        if valid(bo, i, (row, col)): # check if those numbers are valid solutions
            bo[row][col] = i # if valid, add it into the board

            if solve(bo):
                return True

            bo[row][col] = 0 # resets element to 0 because the current number isn't correct

    return False

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])): # go through each element in the row (row, col)
        if bo[pos[0]][i] == num and pos[1] != i: # see if it is equals to the num that we just added in and ignore the position of last insert
            return False

    # Check column
    for i in range(len(bo)): # go through each element in the col (row, col)
        if bo[i][pos[1]] == num and pos[0] != i: # see if it is equals to the num that we just added in and ignore the position of last insert
            return False

    # Check box
    box_x = pos[1] // 3 # col // 3
    box_y = pos[0] // 3 # row // 3

    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

# print board function
def print_board(bo):
    # When i is divisible by 3 print horizontal lines to create board
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        # get length of rows in board[0]
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            # check if at the last position
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="") # end="" means to stay on the same line and keep printing

# Locate empty square in the given board (0) and return that position if found
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])): # length of each row
            if bo[i][j] == 0: # 0 equals empty cell
               return (i, j) # row,col
    return None

print("Sudoku Board")
print_board(board)
solve(board)
print("\n_______________________\n")
print("Solved")
print_board(board)