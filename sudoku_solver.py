import pygame, time
import display

pygame.init()

board = [[7,8,0,4,0,0,1,2,0],
         [6,0,0,0,7,5,0,0,9],
         [0,0,0,6,0,1,0,7,8],
         [0,0,7,0,4,0,2,6,0],
         [0,0,1,0,5,0,9,3,0],
         [9,0,4,0,6,0,0,0,5],
         [0,7,0,3,0,0,0,1,2],
         [1,2,0,0,0,7,4,0,0],
         [0,4,9,2,0,6,0,0,7]]

         
extreme = [[8,5,0,0,7,0,4,0,0],
           [0,0,0,0,0,3,0,0,0],
           [0,9,0,0,0,4,0,0,1],
           [0,0,9,0,1,0,0,8,0],
           [0,4,0,3,0,8,0,7,0],
           [0,3,0,0,4,0,5,0,0],
           [4,0,0,2,0,0,0,1,0],
           [0,0,0,8,0,0,0,0,0],
           [0,0,7,0,3,0,0,2,8]]

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)

    return None


def check(board, num, pos):
    # pos conatains row index and column index of num to be checked
    row_i, column_i = pos

    # check row
    for column in range(len(board[0])):
        if board[row_i][column] == num and column != column_i:
            return False

    # check column
    for row in range(len(board)):
        if board[row][column_i] == num and row != row_i:
            return False

    # check grid
    sq_row = row_i//3
    sq_column = column_i//3

    for i in range(sq_row*3, sq_row*3+3):
        for j in range(sq_column*3, sq_column*3+3):
            if board[i][j] == num and (i,j) != (row_i, column_i):
                return False

    return True


def solve(board):
    empty_pos = find_empty(board)

    if not empty_pos:
        return True
    else:
        row_i, column_i = empty_pos


    for num in range(1,10):
        if check(board, num, (row_i, column_i)):
            board[row_i][column_i] = num        
            display.nums(num, row_i, column_i)
            pygame.display.update()
            time.sleep(0.1)

            if solve(board):
                return True

            check_quit()

            board[row_i][column_i] = 0
            display.empty_cell(row_i, column_i)

    return False


def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return -1

    return 0


def main(board):
    once = True
    running = True
    while running:
        if once:
            display.board(board)
            pygame.display.update()
            solve(board)
            once = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            
    
    return 0


if __name__ == "__main__":
    main()

