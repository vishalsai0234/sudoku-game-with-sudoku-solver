import pygame
from sudokuSolverAlgo import *
from chooseLevel import *
import time
import sys

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
L_GREEN = (150, 255, 150)
RED = (255, 0, 0)
L_RED = (255, 204, 203)
GRAY = (60, 60, 60)
L_GRAY = (220, 220, 220)
YELLOW = (255, 255, 0)

# This sets the WIDTH and HEIGHT of each grid location
HEIGHT = 50
WIDTH =50


# This sets the margin between each cell
MARGIN = 5
numbers_1to9 = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8,
                pygame.K_9]

# Set the width and height of the screen [width, height]
size = (500, 560)
# screen = pygame.display.set_mode(size)
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)

# pygame.display.set_caption("Sudoku King")

# Loop until the user clicks the close button.
done = False
game_over = False  # Flag to track game state (loss)
#print if win
def print_won():
    font = pygame.font.Font(None, 36)
    text = font.render("You Win!", True, RED)
    text_rect = text.get_rect(center=(250, 250))
    screen.blit(text, text_rect)
    pygame.display.flip()

#print if loss
def print_loss():
    font = pygame.font.Font(None, 36)
    text = font.render("You Lost!", True, RED)
    text_rect = text.get_rect(center=(250, 250))
    screen.blit(text, text_rect)
    pygame.display.flip()

def cheatingAllTheWay(sol): 
    for row in range(len(Board)):
        for column in range(len(Board[row])):
            if Board[row][column] == 0:  # Update unsolved locations
                Board[row][column] = sol[row][column]  # Use the solution to update board
                addNumToBoard(Board[row][column], row, column, L_GREEN)
                time.sleep(0.05)
    pygame.display.flip()  # Update the display after filling all cells
    return




def addNumToBoard(number, row, column, color):
    addNewRect(row, column, WHITE, 5)
    addNewRect(row, column, color, None)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(number), True, BLACK, )
    textRect = text.get_rect()  # get_rect() -> Returns a new rectangle covering the entire surface.
    textRect.center = ((MARGIN + WIDTH) * column + MARGIN + WIDTH / 2, (MARGIN + HEIGHT) * row + MARGIN + WIDTH / 2)
    screen.blit(text, textRect)
    drawTheBorder()


def finish(sol):
     
    if sol == Board: #Check if the state of the board is same as the solution.
        print("good")
    else:
        print("not good")


def addNewRect(row, col, color, width):
    rectSize = pygame.Rect((MARGIN + WIDTH) * col + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH,
                           HEIGHT)
    if width is not None:
        pygame.draw.rect(screen, color, rectSize, width)  # coloring only the border
    else:
        pygame.draw.rect(screen, color, rectSize)  # coloring the whole rectangle


def flickering(timeFlickering, color):  # flickering with color on-off
    addNewRect(row, column, color, 5)
    pygame.display.flip()
    time.sleep(timeFlickering)
    addNewRect(row, column, WHITE, 5)
    pygame.display.flip()
    time.sleep(timeFlickering)
    addNewRect(row, column, color, 5)
    pygame.display.flip()
    time.sleep(timeFlickering)
    addNewRect(row, column, WHITE, 5)
    pygame.display.flip()


def drawTheBorder():
    dif = 500 // 9
    for i in range(10):
        thick = 5
        pygame.draw.line(screen, GRAY, (0, i * dif + 2), (500, i * dif + 2), thick)#horizontal line #surface,color ,starting point,end point,width
        pygame.draw.line(screen, GRAY, (i * dif + 2, 0), (i * dif + 2, 500), thick)#verticle
    for i in range(10):
        if i % 3 == 0:
            thick = 8
            pygame.draw.line(screen, BLACK, (0, i * dif), (500, i * dif), thick)
            pygame.draw.line(screen, BLACK, (i * dif, 0), (i * dif, 500), thick)


def drawInitBoard():
    # printBoard(solvedBoard)
    for row in range(len(Board)):
        for column in range(len(Board[row])):
            color = L_GRAY
            if Board[row][column] == 0:  # if we want to change to background of the empty cells
                color = WHITE
                # ----- drawing the rect ------
            pygame.draw.rect(screen, color,
                             [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
            # show nothing if the number is 0
            font = pygame.font.Font('freesansbold.ttf', 32)
            if Board[row][column] == 0:
                text = font.render(" ", True, BLACK, )  # render(text, anti-alias[True], color, background=None)
            else:
                text = font.render(str(Board[row][column]), True, BLACK, )

            textRect = text.get_rect()  # get_rect() -> Returns a new rectangle covering the entire surface.
            textRect.center = (
                (MARGIN + WIDTH) * column + MARGIN + WIDTH / 2, (MARGIN + HEIGHT) * row + MARGIN + WIDTH / 2)
            screen.blit(text, textRect)
            drawTheBorder()
    
    

# -------- Main Program Loop -----------
if __name__ == "__main__":

    print("enter 1 for playing the game :")
    print("Enter 2 for solution of particular game :")
    choise=int(input())
    if choise==1:
        flag1 = True

        while flag1:
            level = chooseLevel()
            if level == 1 or level == 2 or level == 3 or level==4:
                print(level)
                flag1 = False
        pygame.display.set_caption("Sudoku King1")
        screen = pygame.display.set_mode(size)
        lower_rect = pygame.Rect(300, 500, 500, 600)
        lower_life_rect=pygame.Rect(0, 500, 300, 400)

        sol = mainSolver(level)  # first at all the script solve the sudoku by itself

        print("solveBoard")
        printBoard(sol)

        # ------ draw the board ------
        pygame.init()
        screen.fill(BLACK)
        drawInitBoard()
        readyForInput = False
        key = None
        wrong = 0
        game_over=False
        start_time = pygame.time.get_ticks()
        while not done:
            # --- Main event loop
            #adding timmer 
            if not game_over:
                elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
            
        # Do not update elapsed_time anymore when game_over is True
               

            font = pygame.font.Font(None, 36)
            timer_text = font.render("Time: {} sec".format(elapsed_time), True, BLACK)
            screen.fill(WHITE,lower_rect)
            text_rect = timer_text.get_rect(center=(420, 530))
            screen.blit(timer_text, text_rect)
            pygame.display.flip()
            pygame.display.update()

            # life line secreen
            screen.fill(WHITE,lower_life_rect)
            font = pygame.font.Font(None, 36)
            timer_text = font.render("Wrong: {}/3".format(wrong), True, RED)
            
            text_rect = timer_text.get_rect(center=(70, 530))
            screen.blit(timer_text, text_rect)
            pygame.display.flip()
            pygame.display.update()

        
            #if wrong move equals to 3 then game finish
            if(wrong==3):
                game_over=True
                print_loss()

            find = findEmpty(Board)
            if find is None and sol==Board:  # If find is None, all cells are filled, so return True
                game_over=True
                if wrong!=3:          # if user did not mistake 3 times then print won
                    print_won()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:  #for cancel the game
                    done = True
            

                if event.type == pygame.KEYDOWN:
                    if event.key in numbers_1to9:
                        key = chr(event.key)
                    if event.key == pygame.K_RETURN:
                        finish(sol)
                    if event.key == pygame.K_c: #Press 'c' to auto solve the whole board. 
                        cheatingAllTheWay(sol)
                    # Inside the event handling loop
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_h and readyForInput:  # Check if 'h' key is pressed and a cell is selected
                            addNumToBoard(sol[row][column], row, column, YELLOW)  # Show the answer for the selected box

                    
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # ------ if clicked on a cell get his row and column ------
                    if readyForInput is True:
                        addNewRect(row, column, WHITE, None)
                        drawTheBorder()
                        readyForInput = False

                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (WIDTH + MARGIN)
                    # ------ checking if it is a empty (0 inside) ------
                    if Board[row][column] == 0:
                        # ------ coloring the border of the clicked cell ----- #TODO YELLOW
                    
                        addNewRect(row, column, YELLOW, 5)
                        readyForInput = True
                        # ------ now only wait for input from the user -----
                    
                
            if readyForInput and key is not None:
                # ------ checking if the key is good at it's place ------
                if int(key) == sol[row][column]:
                    Board[row][column] = key
                    flickering(0.1, GREEN)  # flickering at a 0.2 seconds with the color green
                    addNumToBoard(key, row, column, L_GREEN)
                else:
                    flickering(0.1, RED)  # flickering at a 0.2 seconds with the color red
                    addNumToBoard(key, row, column, L_RED)
                    wrong+=1

                # -----------------------------------------------
                drawTheBorder()
                readyForInput = False
            
            
            
            # pygame.display.flip()
            # pygame.display.update()
            

            key = None
            pygame.display.flip()
            pygame.display.update()
            pygame.time.delay(100) 

        

    
    # Close the window and quit.
    

    elif choise==2:
    
        pygame.display.set_caption("Sudoku King1")
        screen = pygame.display.set_mode(size)
        lower_rect = pygame.Rect(0, 500, 500, 60)
        

        

        

        # ------ draw the board ------
        pygame.init()
        screen.fill(BLACK)
        drawInitBoard()
        readyForInput = False
        key = None

        
    
        
        while not done:
            # --- Main event loop
            font = pygame.font.Font(None, 36)
            timer_text = font.render("For Solution Enter S ", True, BLACK)
            screen.fill(WHITE,lower_rect)
            text_rect = timer_text.get_rect(center=(280, 530))
            screen.blit(timer_text, text_rect)
            pygame.display.flip()
            pygame.display.update()
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #cancel the soln
                    done = True
            

                if event.type == pygame.KEYDOWN:
                    if event.key in numbers_1to9:
                        key = int(chr(event.key))

                    if event.key == pygame.K_s: #Press 's' to  solve the whole board. 
                        print(Board)
                        sol =solver(Board)
                        cheatingAllTheWay(sol)
                    
                        
                
                    
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # ------ if clicked on a cell get his row and column ------
                    if readyForInput is True:
                        addNewRect(row, column, WHITE, None)
                        drawTheBorder()
                        readyForInput = False

                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (WIDTH + MARGIN)
                    # ------ checking if it is a empty (0 inside) ------
                    if Board[row][column] == 0:
                        # ------ coloring the border of the clicked cell ----- #TODO YELLOW
                    
                        addNewRect(row, column, YELLOW, 5)
                        readyForInput = True
                        # ------ now only wait for input from the user -----
                    
                
            if readyForInput and key is not None:
                # ------ checking if the key is good at it's place ------
                
                Board[row][column] = key
                flickering(0.1, GREEN)  # flickering at a 0.2 seconds with the color green
                addNumToBoard(key, row, column, WHITE)
                
                

                # -----------------------------------------------
                drawTheBorder()
                readyForInput = False
            
            
            
        
            

            key = None
            pygame.display.flip()
            pygame.display.update()
            pygame.time.delay(100) 

        

    
    # Close the window and quit.
    pygame.quit()




        