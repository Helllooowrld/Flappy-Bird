import pygame as pg
from sys import exit
import Bird 

pg.init()

x1 = 0
x2 = 0
screen = pg.display.set_mode((350, 700))
clock = pg.time.Clock()
sky = pg.image.load('./sprites/background-day.png')
ground = pg.image.load('./sprites/base.png')
transformedSky = pg.transform.scale(sky, (400, 711.11))
transformedGround = pg.transform.scale(ground, (400, 133.33))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.blit(transformedSky, (x1, 0))
    screen.blit(transformedSky, (x2, 0))

    transformedSky.blit(transformedGround, (x1, 570))
    transformedSky.blit(transformedGround, (x2, 570))
    x1 -= 1
    if x1 < -10:
        x2 = x1+400
    x2 -= 1
    if x2 < -10:
        x1 = x2+400
    bird=pg.sprite.GroupSingle()
    bird.add(Bird.birdClass())
    bird.draw(screen)
    pg.display.update()
    clock.tick(60)
