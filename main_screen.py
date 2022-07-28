import pygame
import display, sudoku_solver
from test_cases import test_cases

pygame.init()

board1 = [
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

# board = test_cases['medium_3']
board = board1


click = True
def main():
    once = True
    running = True
    while running:
        if once:
            result = display.solve_screen(board)
            if result == 1:
                result = sudoku_solver.main(board)  
                once = False
                if result == -1:
                    running = False
                if result == 0:
                    running = False
                
            if result == -1:
                    running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
    
    pygame.quit()


if __name__ == "__main__":
    main()
