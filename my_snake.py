from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
running = True #variable booléenne

while running:
    clock.tick(1)

    for event in pg.event.get():
        if event.type == pg.QUIT:
                running = False
        if event.type == pg.KEYDOWN: # on teste si l'évènement est une touche pressée
             if event.key == pg.K_q:  # on teste si la touche est q
                running = False

    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.fill(random_color)
    pg.display.update()

pg.quit() #on ferme la fenêtre
sys.exit()