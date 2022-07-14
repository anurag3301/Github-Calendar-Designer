import pygame
import datetime
import pickle
from dateutil.relativedelta import relativedelta
import sys
import utils
 
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
BTN_BG = (40, 40, 40)
BTN_FG = (200, 200, 200)

pygame.init()

def grid_creator(year, old=False):
    grid = []

    if old:
        try:
            with open(f'{year}.pkl', 'rb') as f:
                grid = pickle.load(f)
            return grid
        except FileNotFoundError:
            pass

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

    
def grid_screen_init(year): 
    screen = pygame.display.set_mode(WINDOW_SIZE)
    done = False
    clock = pygame.time.Clock()
    
    grid = grid_creator(year)

    old_button = utils.button(BTN_BG, BTN_FG, 400, 195, 70, 40, ' Old ')
    save_button = utils.button(BTN_BG, BTN_FG, 570, 195, 220, 40, ' Save And Exit ')
    start_button = utils.button(BTN_BG, BTN_FG, 900, 195, 100, 40, ' Start ')

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if old_button.isOver(pos):
                    grid = grid_creator(year, old=True)

                if save_button.isOver(pos):
                    with open(f'{year}.pkl', 'wb') as f:
                        pickle.dump(grid, f)
                    exit()

                if start_button.isOver(pos):
                    return grid

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

        old_button.draw(screen)
        save_button.draw(screen)
        start_button.draw(screen)
     
        clock.tick(60)
     
        pygame.display.flip()

    pygame.quit()
    return []

def get_dates(year):
    grid = grid_screen_init(year)

    if len(grid) == 0:
        exit()

    fday = datetime.datetime(year, 1, 1).weekday()
    fday = -1 if fday == 6 else fday

    dates_list=[]

    for i in range(COLS):
        for j in range(ROWS):
            if grid[i][j]==True:
                date = datetime.date(year, 1, 1) + relativedelta(weeks=+i, days=+(j-fday-1))
                dates_list.append(date)

    return dates_list

if __name__=="__main__":
    year = 2019
    print(get_dates(year))
