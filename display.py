import pygame
import time

pygame.init()

# Screen Definition
WINDOW_WIDTH, WINDOW_HEIGHT = 700,700
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set Caption
pygame.display.set_caption("Sudoku Solver")

# Font
FONT = {25: pygame.font.SysFont("cascadia code", 25),
        30: pygame.font.SysFont("cascadia code", 30)}



def display_blue_nums():
    WINDOW.fill((255,255,255))


def board_lines():
    # displaying lines on board
    x1 = y1 = 125
    for i in range(10):

        if i%3==0:
            width_of_line = 3
        else:
            width_of_line = 1
        
        # vertical lines
        pygame.draw.line(WINDOW, (0,0,0), (x1,125), (x1,575), width_of_line)
        # horizontal lines
        pygame.draw.line(WINDOW, (0,0,0), (125,y1), (575,y1), width_of_line)
        
        x1+=50
        y1+=50


# coordinate list of positions for nums
x = [i for i in range(145, 575, 50)]
y = [j for j in range(145, 575, 50)]

def nums(num, num_i, num_j):
    WINDOW.blit(FONT[25].render(f"{num}", 1, (0,0,255), (255,255,255)), (y[num_j], x[num_i]))
    pygame.display.update()


def empty_cell(cell_i,cell_j):
    cell = pygame.Rect(y[cell_j]-16, x[cell_i]-17, 43, 43)
    pygame.draw.rect(WINDOW, (255,255,255), cell)
    pygame.display.update()
    time.sleep(0.1)


def highlight_cell(cell_i, cell_j):
    cell = pygame.Rect(y[cell_j]-16, x[cell_i]-17, 43, 43)
    pygame.draw.rect(WINDOW, (255,255,255), cell)
    pygame.display.update()
    time.sleep(0.1)


def board(bo):
    WINDOW.fill((255,255,255))
    board_lines()
    # dislaying numbers on board
    x1 = y1 = 145
    for i in range(9):
        for j in range(9):

            disp_num = bo[i][j] if bo[i][j]!=0 else " "

            WINDOW.blit(FONT[25].render(f"{disp_num}", 1, (0,0,0)), (x1,y1))
            x1+=50

        x1 = 145
        y1+=50
    # pygame.display.update()

solve_button = pygame.Rect(300,600,100,50)

click = False 
def solve_screen(bo):
    running = True
    while running:
        
        board(bo)
        pygame.draw.rect(WINDOW,(0,0,0), solve_button, border_radius=5)
        WINDOW.blit(FONT[30].render("Solve",1,(255,255,255)), (323,615))
        pygame.display.update()
        
        mx,my = pygame.mouse.get_pos()
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True  


        if click:
            if solve_button.collidepoint((mx,my)):
                return 1

    return 0



# if __name__ == "__main__":
    # main()

