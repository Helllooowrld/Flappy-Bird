import pygame as pg
from sys import exit
import Bird
import Pipes
import Score

pg.init()

x1 = 0
x2 = 0
screen = pg.display.set_mode((350, 700))
clock = pg.time.Clock()
sky = pg.image.load('./sprites/background-day.png')
ground = pg.image.load('./sprites/base.png')
transformedSky = pg.transform.scale(sky, (400, 711.11))
transformedGround = pg.transform.scale(ground, (400, 133.33))

bird = pg.sprite.GroupSingle()
bird.add(Bird.birdClass())

pipe = pg.sprite.Group()
pipeSpawn = 0
pipePassed = False

score = 0
score_group = pg.sprite.Group()

def collision():
    if pg.sprite.spritecollide(bird.sprite, pipe, True):
        pg.quit()
        exit()


while True:
    score_group.empty()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.blit(transformedSky, (x1, 0))
    screen.blit(transformedSky, (x2, 0))

    transformedSky.blit(transformedGround, (x1, 570))
    transformedSky.blit(transformedGround, (x2, 570))
    x1 -= 2
    if x1 < -20:
        x2 = x1+400
    x2 -= 2
    if x2 < -20:
        x1 = x2+400

    if pipeSpawn == 0:
        pipe.add(Pipes.pipeClass("Down"))
        pipe.add(Pipes.pipeClass("Up"))
    elif pipeSpawn >= 5:
        pipeSpawn = -0.1
    pipeSpawn += 0.1

    bird.draw(screen)
    bird.update()
    pipe.draw(screen)
    pipe.update()
    temp=score
   

    
    for i in range(0,len(str(score))):
            score_group.add(Score.scoreClass(i))
            rem=temp%10
            temp=int(temp/10)
            score_group.sprites()[i].update(rem)
            
            
    

    collision()

    for i in pipe:
        if not pipePassed and i.rect.left < bird.sprites()[0].rect.left and i.rect.right > bird.sprites()[0].rect.right:
            pipePassed = True
        if pipePassed and i.rect.right < bird.sprites()[0].rect.left:
            pipePassed = False
            score += 1
       
    

    score_group.draw(screen)
    pg.display.update()
   
    clock.tick(60)
