import pygame
import datetime
 
WINDOW_SIZE = [1400, 255]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WIDTH = 20
HEIGHT = 20
ROWS = 7
COLS = 53
MARGIN = 5

pygame.init()

def grid_creator(year):
    grid = []
    for row in range(COLS):
        grid.append([])
        for column in range(ROWS):
            grid[row].append(False)
 
    fday = datetime.datetime(year, 1, 1).weekday()
    lday = datetime.datetime(year, 12, 31).weekday()
    if(fday!=6):
        for i in range(fday+1):
            grid[0][i] = None
     
    if(lday!=5):
        lday = -1 if lday == 6 else lday
        for i in range(lday+2, 7):
            grid[-1][i] = None

    return grid

    
def grid_screen_init(): 
    screen = pygame.display.set_mode(WINDOW_SIZE)
    done = False
    clock = pygame.time.Clock()
    grid = grid_creator(2019)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                if pos[0]<(MARGIN + WIDTH) * 53 and pos[1]<(MARGIN + HEIGHT) * 7:
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    if(grid[column][row]!=None):
                        grid[column][row] = not grid[column][row]
     
        screen.fill(BLACK)
     
        for row in range(COLS):
            for column in range(ROWS):
                color = WHITE
                if grid[row][column] == True:
                    color = GREEN
                if grid[row][column] == None:
                    color = BLACK
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * row + MARGIN,
                                  (MARGIN + HEIGHT) * column + MARGIN,
                                  WIDTH,
                                  HEIGHT])
     
        clock.tick(60)
     
        pygame.display.flip()

    pygame.quit()
    return grid

if __name__=="__main__":
    grid = grid_screen_init()
    print(grid)
