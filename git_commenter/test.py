import pygame
import datetime
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
WIDTH = 20
HEIGHT = 20
ROWS = 7
COLS = 53
 
MARGIN = 5
grid = []
for row in range(COLS):
    grid.append([])
    for column in range(ROWS):
        grid[row].append(False)  # Append a cell
 
pygame.init()
 
WINDOW_SIZE = [1400, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
pygame.display.set_caption("Array Backed Grid")
 
done = False
 
clock = pygame.time.Clock()

year = 2019
fday = datetime.datetime(year, 1, 1).weekday()
lday = datetime.datetime(year, 12, 31).weekday()
if(fday!=6):
    for i in range(fday+1):
        grid[0][i] = None
 
if(lday!=5):
    lday = -1 if lday == 6 else lday
    for i in range(lday+2, 7):
        grid[-1][i] = None

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
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
 
print(grid)

pygame.quit()
