from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
running = True #variable booléenne

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

while running:
    clock.tick(1)

    for event in pg.event.get():
        if event.type == pg.QUIT:
                running = False
        if event.type == pg.KEYDOWN: # on teste si l'évènement est une touche pressée
             if event.key == pg.K_q:  # on teste si la touche est q
                running = False
    
    screen.fill((0,0,0))   #écran noir         
    
    draw_board()
    pg.display.update()

pg.quit() #on ferme la fenêtre
sys.exit()


          
