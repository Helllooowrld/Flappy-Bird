import pygame as pg
from sys import exit
import Bird
import Pipes
import Score

pg.init() 
start=True
restart=True
x1 = 0
x2 = 0 
White=(255,255,255)
Black=(0,0,0)
screen = pg.display.set_mode( (350, 700))
clock = pg.time.Clock()
sky = pg.image.load('C:/Users/DELL/Desktop/New folder/Flappy-Bird/sprites/background-day.png')
ground = pg.image.load('C:/Users/DELL/Desktop/New folder/Flappy-Bird/sprites/base.png')
home_screen_img=pg.image.load('C:/Users/DELL/Desktop/New folder/Flappy-Bird//sprites/message.png')
home_screen_rect=home_screen_img.get_rect(center=(175,350))
transformedSky = pg.transform.scale(sky, (400, 711.11))
transformedGround = pg.transform.scale(ground, (400, 133.33))
gameOver=pg.image.load('C:/Users/DELL/Desktop/New folder/Flappy-Bird/sprites/gameover.png')

bird = pg.sprite.GroupSingle()
bird.add(Bird.birdClass())

pipe = pg.sprite.Group()
pipeSpawn = 0
pipePassed = False

score = 0
highest_score=0
score_group = pg.sprite.Group()

def home_screen():
    global start
    while start:
        screen.blit(home_screen_img,home_screen_rect)
        for event in pg.event.get():
            if event.type==pg.KEYDOWN :
                    print('key press')
                    if event.key == pg.K_SPACE:
                        start=False
        pg.display.update()
                        
                    
def draw_highest_score_image(highest_score, surface, pos_x, pos_y):
        score_str = str(highest_score)
        digit_sprites = []

    # Create digit sprites for each digit (right to left)
        for i, digit_char in enumerate(reversed(score_str)):
            digit = int(digit_char)
            digit_sprite = Score.scoreClass(i)  # position index i
            digit_sprite.update(digit)
            digit_sprite.rect.midtop = (pos_x - 26 * i, pos_y)  # position each digit spaced by 26 pixels
            digit_sprites.append(digit_sprite)

    # Draw digits on the given surface
        for digit_sprite in digit_sprites:
            print('working')
            screen.blit(digit_sprite.image, digit_sprite.rect)

def reset_game():
    global score, pipePassed, pipeSpawn, restart,start
    
    score = 0
    pipePassed = False
    pipeSpawn = 0
    
    pipe.empty()  # Remove all existing pipes
    
    bird.empty()
    bird.add(Bird.birdClass())  # Reset bird to starting state
    
    score_group.empty()  # Clear score sprites
    start=True
    restart = True

def collision():
    global highest_score
    
    if pg.sprite.spritecollide(bird.sprite, pipe, True):
        if score>highest_score:
            highest_score=score
        global restart 
        restart=False
        draw_highest_score_image(highest_score,screen,180,250)
        screen.fill(Black)
        
        font_reset=pg.font.SysFont('C:/Users/DELL/Desktop/New folder/Flappy-Bird/fonts/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf',30)
        text_surface_reset=font_reset.render("Press Enter To RESTART",False,White)
        text_rect_restart=text_surface_reset.get_rect(center=(180,350))
        
        gameOver_rect=gameOver.get_rect(center=(180,300))
        screen.blit(gameOver,gameOver_rect)
        screen.blit(text_surface_reset,text_rect_restart)
        pg.display.flip()
        
        while True:
            for event in pg.event.get():
                if event.type==pg.KEYDOWN :
                    print('key press')
                    if event.key == pg.K_RETURN:
                        reset_game()
                        return
                elif event.type == pg.QUIT:
                    pg.quit()
                    exit()

           
    
while restart:
    score_group.empty()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        
    screen.blit(transformedSky, (x1, 0))
    screen.blit(transformedSky, (x2, 0))
             
    transformedSky.blit(transformedGround, (x1, 570))
    transformedSky.blit(transformedGround, (x2, 570))
    
    home_screen()
        
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
