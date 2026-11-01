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
FRUIT = (randint(0, 29), randint(0, 29))
SCORE = 0


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
          pg.draw.line(screen, color=(255,0,0), start_pos=start, end_pos=end, width=5)


def move_snake(snake, direction):
     snake.append((snake[2][0]+direction[0],snake[2][1]+direction[1]) )
     snake.pop(0)
     return snake

def draw_fruit(fruit):
    case = pg.Rect(fruit[0]*20, fruit[1]*20, 20, 20)
    pg.draw.rect(screen, (0, 255, 0), case)


def eat_fruit(score, snake, fruit):
    f = fruit
    if snake[-1] == fruit:
        score += 1
        f = (randint(0, 29), randint(0, 29))
        snake.insert(0, (snake[0][0]-1,snake[0][1]-1))
    return (score, snake, f)

score, snake, fruit = eat_fruit(0, [(10, 15), (11, 15), (12, 15)], (12, 15))
assert score == 1 and len(snake) == 4

score, snake, fruit = eat_fruit(0, [(10, 15), (11, 15), (12, 15)], (0, 0))
assert score == 0 and len(snake) == 3 and fruit == (0, 0)


while running:
    clock.tick(2)

    for event in pg.event.get():
        if event.type == pg.QUIT:
                running = False
        if event.type == pg.KEYDOWN: # on teste si l'évènement est une touche pressée
            if event.key == pg.K_q:  # on teste si la touche est q
                running = False
            elif event.key == pg.K_UP:
                DIRECTION = (0, -1) # il faut enlever 1 car l'axe des ordonnées est orienté vers le bas 
            elif event.key == pg.K_DOWN:
                DIRECTION = (0, 1)
            elif event.key == pg.K_LEFT:
                DIRECTION = (-1, 0)
            elif event.key == pg.K_RIGHT:
                DIRECTION = (1, 0)
    
    screen.fill((0,0,0))   #écran noir         
    
    draw_board()
    draw_snake(SNAKE)
    move_snake(SNAKE, DIRECTION) #Lorsque le serpent atteint le bord du cadre, il disparait de l'image
    eat_fruit(SCORE,SNAKE,FRUIT)
    draw_fruit(FRUIT)
    pg.display.update()

pg.quit() #on ferme la fenêtre
sys.exit()


          
