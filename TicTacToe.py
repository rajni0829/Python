import pygame,sys
import numpy as np

# Initialising pygame
pygame.init()

# Initializing Constants
WIDTH         = 700
HEIGHT        = WIDTH
LINE_WIDTH    = 15
BOARD_ROWS    = 3
BOARD_COLS    = 3
SQUARE_SIZE   = WIDTH//BOARD_COLS
SPACE         = SQUARE_SIZE//4      # space b/w each square corner & crossline
CIRCLE_RADIUS = SQUARE_SIZE//3
CIRCLE_WIDTH  = 15
CROSS_WIDTH   = 25


# Color codes
LINE_COLOR     = (255,0,0)
BG_COLOR       = (0,0,0)
BLACK          = (0,0,0)
RED            = (255,0,0)
WHITE          = (255,255,255)
CIRCLE_COLOR   = (253, 253, 150)
CROSS_COLOR    = (0, 181, 184)


# Creating Screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')          # Adding Title
screen.fill(BG_COLOR)                              # adding color


# Creating board
board = np.zeros((BOARD_ROWS,BOARD_COLS))


# func to draw main 4 Lines to play
def drawLines():
    # parameters : screen, color, starting pos ,ending, width
    pygame.draw.line(screen,WHITE,(0,SQUARE_SIZE),(WIDTH,SQUARE_SIZE),LINE_WIDTH)         # horizontal1
    pygame.draw.line(screen,WHITE,(0,2*SQUARE_SIZE),(WIDTH,2*SQUARE_SIZE),LINE_WIDTH)     # horizontal2
    pygame.draw.line(screen,WHITE,(SQUARE_SIZE,0),(SQUARE_SIZE,HEIGHT),LINE_WIDTH)        # vertical1
    pygame.draw.line(screen,WHITE,(2*SQUARE_SIZE,0),(2*SQUARE_SIZE,HEIGHT),LINE_WIDTH)    # vertical2


def drawFigures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):

            # if its player1 use "O" , if val==1 means player has marked his turn
            if board[row][col] == 1:  
                pygame.draw.circle(screen,CIRCLE_COLOR,(int(col * SQUARE_SIZE + SQUARE_SIZE//2),int(row * SQUARE_SIZE + SQUARE_SIZE//2)),CIRCLE_RADIUS,CIRCLE_WIDTH)    #drawing circle in the centre of x axis
            
            elif board[row][col] == 2:
                pygame.draw.line(screen,CROSS_COLOR,(col*SQUARE_SIZE+SPACE,row*SQUARE_SIZE+SQUARE_SIZE-SPACE),(col*SQUARE_SIZE+SQUARE_SIZE-SPACE,row*SQUARE_SIZE+SPACE),CROSS_WIDTH)

                pygame.draw.line(screen,CROSS_COLOR,(col*SQUARE_SIZE+SPACE,row*SQUARE_SIZE+SPACE),(col*SQUARE_SIZE+SQUARE_SIZE-SPACE,row*SQUARE_SIZE+SQUARE_SIZE-SPACE),CROSS_WIDTH)


def markSquare(row,col,player):          # marks coordinates in the box
    board[row][col] = player             # OR replace 0 with player in (row,col) coordinate


def availableSquare(row,col):            # returns TRUE if availabe else FALSE
    return board[row][col] == 0          
    

def isBoardFull():                       # traverse each square & check whether available
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return  False

    return True


def checkWin(player):
    #vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            drawVerticalWinningLine(col,player)
            return True

    # horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            drawHorizontalWinningLine(row,player)
            return True

    # ascending diagonal winning check
    if board[2][0] == player and board[1][1]== player and board[0][2] == player:
        drawAscDiagonal(player)
        return True

    if board[0][0] == player and board[1][1]== player and board[2][2] == player:
        drawDescDiagonal(player)
        return True


def drawVerticalWinningLine(col,player):
    posX = col*SQUARE_SIZE + SQUARE_SIZE//2                    # since vert so X pos wont change
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen,color,(posX,15),(posX,HEIGHT-15),15)


def drawHorizontalWinningLine(row,player):
    posY = row*SQUARE_SIZE+SQUARE_SIZE//2                    # since horiz so Y pos wont change
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen,color,(15,posY),(WIDTH-15,posY),15)


def drawAscDiagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(screen,color,(15,HEIGHT-15),(WIDTH-15,15),15)


def drawDescDiagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT-15),15)


def restart():
    screen.fill(BG_COLOR)
    drawLines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

drawLines()



# Driver code
player = 1
gameOver = False

while True:
    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            sys.exit()

        # checking if we're clicking the screen ?
        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
            
            mouseX = event.pos[0]                           # accessing x  coordinate
            mouseY = event.pos[1]                           # accessing y coordinate


            clickedRow = int(mouseY // SQUARE_SIZE)         #len of each sq = SQUARE_SIZE
            clickedCol = int(mouseX // SQUARE_SIZE)
            

            if availableSquare(clickedRow, clickedCol):
                markSquare(clickedRow,clickedCol,player)
                if checkWin(player):
                    print("Player{} Wins".format(player))
                    gameOver = True
                player = player % 2 + 1                    # changes player name

                drawFigures()

        if event.type == pygame.KEYDOWN:                  # whether user clicks a key
            if event.key == pygame.K_r:
                restart()
                gameOver = False


    pygame.display.update()

print("\n")