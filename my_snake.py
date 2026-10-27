from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

while True:
    clock.tick(1)

    for event in pg.event.get():
        if event.type == pg.QUIT:
                pg.quit()     #On ajoute ces lignes pour pouvoir fermer la fenêtre, sinon elle reste toujours ouverte.
                sys.exit()

    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.fill(random_color)
    pg.display.update()
