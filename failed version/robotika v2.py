import pygame
pygame.init()

'''
Tugas UTS Instrumrntasi Sistem Robotika
Mahatma Ageng Wisesa
17/411372/TK/45857
'''

# Resolusi Layar
rel = 600
# pixel grid
grid = 40

win = pygame.display.set_mode((rel, rel))
pygame.display.set_caption('UTS Robotika (Finite State Machine)')
clock = pygame.time.Clock()

# Character
charWidth = 40
charHeight = 40
char = pygame.image.load('img/terminator.png')
char = pygame.transform.scale(char, (charWidth, charHeight))

class robot(object):
    def __init__(self, x, y, width, height):
        self.x1 = x 
        self.y1 = y

        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0

    def draw(self):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
            
        if self.left:
            win.blit(char, (self.x1, self.y1))
            self.walkCount +=1
        elif self.right:
            win.blit(char, (self.x1, self.y1))
            self.walkCount +=1
        elif self.up:
            win.blit(char, (self.x1, self.y1))
            self.walkCount +=1
        elif self.down:
            win.blit(char, (self.x1, self.y1))
            self.walkCount +=1
        else:
            win.blit(char, (self.x1, self.y1))

class barrier(object):
    def __init__(self, x , y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
    
    def draw(self):
        pygame.draw.rect(win, (0, 140, 196), (
            self.x,
            self.y,
            self.height,
            self.width
            ))

# tembok
def tembok():
    barrier(0,0,grid,rel).draw() # Left
    barrier(0,0,rel,grid).draw() # up
    barrier(rel-grid,0,grid,rel).draw() # right
    barrier(0,rel-grid,rel,grid).draw() # down
    
    barrier(4*grid,rel-6*grid,grid,5*grid).draw() # tembok 1
    barrier(grid,6*grid,7*grid,grid).draw() # tembok 2
    barrier(rel-7*grid,6*grid,grid,5*grid).draw() # tembok 3
    barrier(rel-4*grid,3*grid, grid, 8*grid).draw() # tembok 4
    barrier(rel-3*grid,3*grid,2*grid,grid).draw() #tembok 5

    # pintu
    pygame.draw.rect(win, (250, 234, 15), (grid*2,rel-grid,grid,grid))
    pygame.draw.rect(win, (15, 250, 82), (0, 2*grid,grid,grid))

# backgroud
def background():
    win.fill((0, 0, 0))
    tembok()
    # x-y grid
    for i in range(0, rel+1, grid):
        pygame.draw.lines(
            win, (255, 255, 255), False, 
            [(0,i), (rel,i)], 1)
        pygame.draw.lines(
            win, (255, 255, 255), False,
            [(i,0), (i,rel)], 1)

# redraw
def redrawWindow():
    terminator_1.draw()
    pygame.display.update()

# robot
terminator_1 = robot(2*grid, rel-3*grid, grid, grid)

# Main Loop
run = True
while run:
    # FPS
    clock.tick(60)

    # BREAK
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Coords
    x1 = terminator_1.x1; y1 = terminator_1.y1
    x2 = x1+grid; y2 = y1
    x3 = x1+grid; y3 = y1+grid
    x4 = x1; y4 = y1+grid 
    '''
    goLeft = keys[pygame.K_LEFT] 
    goRight = keys[pygame.K_RIGHT]
    goUp = keys[pygame.K_UP] 
    goDown = keys[pygame.K_DOWN]'''

    r_A_y = terminator_1.y1-7*grid #tembok 2
    r_C_y = (rel-grid)-terminator_1.y1 # tembok 2
    r_B_y = (rel-7*grid) - terminator_1.x1

    # Final State Machine
    print('x1:', terminator_1.x1)
    print('y1:', terminator_1.y1)
    print('r_A:', r_A_y) # sensor A
    print('r_C:', r_C_y) # sensor C
    print('r_B:', r_B_y) # sensor B
    print('-----------------------------')

    if (r_A_y>r_C_y):
        goUp = True
        goDown = False
        goLeft = False
        goRight = False

    if (r_A_y == grid-20):
        goUp = False
        goDown = False
        goLeft = False
        goRight = True

    if (
        r_B_y == grid
    ):
        goUp = False
        goDown = True
        goLeft = False
        goRight = True

    # Pergerakan 
    if (
        goLeft
        and (terminator_1.x1 > grid+terminator_1.vel) # tembok barat
        and not(4*grid<x4-terminator_1.vel<5*grid and rel-6*grid<y4<rel-grid) # tembok 1
        and not(grid<x4-terminator_1.vel<8*grid and  6*grid<y4-terminator_1.vel<7*grid) and not(grid<x1-terminator_1.vel<8*grid and  6*grid<y1+terminator_1.vel<7*grid) # tembok 2 #UNTUK DOWN
        and not(rel-7*grid<x1-terminator_1.vel<rel-6*grid and 6*grid<y1-terminator_1.vel<rel-4*grid) and not(rel-7*grid<x4-terminator_1.vel<rel-6*grid and 6*grid<y4+terminator_1.vel<rel-4*grid) # tembok 3
        and not(rel-4*grid<x1-terminator_1.vel<rel-3*grid and 3*grid<y1-terminator_1.vel<rel-4*grid) and not(rel-4*grid<x4-terminator_1.vel<rel-3*grid and 3*grid<y4+terminator_1.vel<rel-4*grid) # tembok 4
        # tembok 5
        ):
        terminator_1.x1 -= terminator_1.vel; 
        terminator_1.left = True
        terminator_1.right = False
        terminator_1.up = False
        terminator_1.down = False
    elif (
        goRight
        and (terminator_1.x1 < rel-grid-terminator_1.width-terminator_1.vel) # tembok timur
        and not(4*grid<x3+terminator_1.vel<5*grid and rel-6*grid<y3<rel-grid) # tembok 1
        and not(rel-7*grid<x2+terminator_1.vel<rel-6*grid and 6*grid<y2<rel-4*grid) and not(rel-7*grid<x3+terminator_1.vel<rel-6*grid and 6*grid<y3-terminator_1.vel<rel-4*grid) # tembok 3
        and not(rel-4*grid<x2+terminator_1.vel<rel-3*grid and 3*grid<y2-terminator_1.vel<rel-4*grid) and not(rel-4*grid<x3+terminator_1.vel<rel-3*grid and 3*grid<y3+terminator_1.vel<rel-4*grid) # tembok 4
        # tembok 5
        ):
        terminator_1.x1 += terminator_1.vel
        terminator_1.right = True
        terminator_1.left = False
        terminator_1.up = False
        terminator_1.down = False
    elif (
        goUp
        and (terminator_1.y1 > grid+terminator_1.vel) # tembok utara
        # tembok 1
        and not(grid<x1-terminator_1.vel<8*grid and  6*grid<y1-terminator_1.vel<7*grid) and not(grid<x2+terminator_1.vel<8*grid and  6*grid<y2-terminator_1.vel<7*grid) # tembok 2
        and not(rel-7*grid<x1+terminator_1.vel<rel-6*grid and 6*grid<y1-terminator_1.vel<rel-4*grid) and not(rel-7*grid<x2-terminator_1.vel<rel-6*grid and 6*grid<y2-terminator_1.vel<rel-4*grid) # tembok 3
        and not(rel-4*grid<x1+terminator_1.vel<rel-3*grid and 3*grid<y1-terminator_1.vel<rel-4*grid) and not(rel-4*grid<x2-terminator_1.vel<rel-3*grid and 3*grid<y2-terminator_1.vel<rel-4*grid) # tembok 4
        and not(rel-3*grid<x1+terminator_1.vel<rel-grid and 3*grid<y1-terminator_1.vel<4*grid) and not(rel-3*grid<x2-terminator_1.vel<rel-grid and 3*grid<y2-terminator_1.vel<4*grid) # tembok 5
        ):
        terminator_1.y1 -= terminator_1.vel
        terminator_1.right = False
        terminator_1.left = False
        terminator_1.up = True
        terminator_1.down = False
    elif (
        goDown 
        and (terminator_1.y1 < rel-grid-terminator_1.height-terminator_1.vel) # tembok selatan
        and not(4*grid<x3-terminator_1.vel<5*grid and rel-6*grid<y3+terminator_1.vel<rel-grid) and not(4*grid<x4+terminator_1.vel<5*grid and rel-6*grid<y4+terminator_1.vel<rel-grid) # tembok 1
        and not(grid<x4-terminator_1.vel<8*grid and  6*grid<y4+terminator_1.vel<7*grid) and not(grid<x3+terminator_1.vel<8*grid and  6*grid<y3+terminator_1.vel<7*grid) # tembok 2
        and not(rel-7*grid<x3<rel-6*grid and 6*grid<y3+terminator_1.vel<rel-4*grid) and not(rel-7*grid<x4<rel-6*grid and 6*grid<y4+terminator_1.vel<rel-4*grid) # tembok 3
        and not(rel-4*grid<x3-terminator_1.vel<rel-3*grid and 3*grid<y3+terminator_1.vel<rel-4*grid) and not(rel-4*grid<x4+terminator_1.vel<rel-3*grid and 3*grid<y4+terminator_1.vel<rel-4*grid) # tembok 4
        and not(rel-3*grid<x3+terminator_1.vel<rel-grid and 3*grid<y3+terminator_1.vel<4*grid) and not(rel-3*grid<x4-terminator_1.vel<rel-grid and 3*grid<y4+terminator_1.vel<4*grid) # tembok 5
        ):
        terminator_1.y1 += terminator_1.vel
        terminator_1.right = False
        terminator_1.left = False
        terminator_1.up = False
        terminator_1.down = True
    else:
        terminator_1.right = False
        terminator_1.left = False
        terminator_1.up = False
        terminator_1.down = False
        terminator_1.walkCount = 0
    '''
    print('x :', x1, x2, x3, x4)
    print('y :', y1, y2, y3, y4)
    print('-------------------')
    '''
    background()
    redrawWindow()
    
pygame.quit()
