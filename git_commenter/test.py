import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
WIDTH = 20
HEIGHT = 20
ROWS = 7
COLS = 52
 
MARGIN = 5
grid = []
for row in range(ROWS):
    grid.append([])
    for column in range(COLS):
        grid[row].append(False)  # Append a cell
 
pygame.init()
 
WINDOW_SIZE = [1400, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
pygame.display.set_caption("Array Backed Grid")
 
done = False
 
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            grid[row][column] = not grid[row][column]
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    screen.fill(BLACK)
 
    for row in range(ROWS):
        for column in range(COLS):
            color = WHITE
            if grid[row][column] == True:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    clock.tick(60)
 
    pygame.display.flip()
 
print(grid)

pygame.quit()
