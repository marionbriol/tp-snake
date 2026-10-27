from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
running = True #variable booléenne
SNAKE = [
   (10, 15),
   (11, 15),
   (12, 15),
]
DIRECTION = (1, 0)   # vers la droite


def draw_board():
     x, y = 0, 0
     a, o = 30, 30
     width, height = 20, 20
     color = (255, 255, 255)
     for i in range(a):
        if i%2 == 0:
             y = 0
        elif i%2==1:
            y = 20
        for j in range(o):
            rect = pg.Rect(x, y, width, height)
            pg.draw.rect(screen, color, rect)
            y += 40
        x += 20
#  15*15 rectangles sont tracés    


def draw_snake(snake):
     for k in range(len(snake)-1):
          start = (snake[k][0]*20,snake[k][1]*20)
          end = (snake[k+1][0]*20,snake[k+1][1]*20)
          pg.draw.line(screen, color=(255,0,0), start_pos=start, end_pos=end)


def move_snake(snake, direction):
     snake.append((snake[2][0]+direction[0],snake[2][1]+direction[1]) )
     snake.pop(0)
     return snake

assert move_snake([(10, 15), (11, 15), (12, 15)], (1, 0)) == [(11, 15), (12, 15), (13, 15)]
assert move_snake([(10, 15), (11, 15), (12, 15)], (0, -1)) == [(11, 15), (12, 15), (12, 14)]


while running:
    clock.tick(2)

    for event in pg.event.get():
        if event.type == pg.QUIT:
                running = False
        if event.type == pg.KEYDOWN: # on teste si l'évènement est une touche pressée
             if event.key == pg.K_q:  # on teste si la touche est q
                running = False
    
    screen.fill((0,0,0))   #écran noir         
    
    draw_board()
    draw_snake(SNAKE)
    move_snake(SNAKE, DIRECTION) #Lorsque le serpent atteint le bord du cadre, il disparait de l'image
    pg.display.update()

pg.quit() #on ferme la fenêtre
sys.exit()


          
