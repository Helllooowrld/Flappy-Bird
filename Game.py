import pygame as pg
from sys import exit
import os
import Bird
import Pipes
import Score

pg.init()

start = True
restart = True
x1 = 0
x2 = 0
White = (255, 255, 255)
Black = (0, 0, 0)
screen = pg.display.set_mode((350, 700))
clock = pg.time.Clock()
sky = pg.image.load("./sprites/background-day.png")
ground = pg.image.load("./sprites/base.png")
home_screen_img = pg.image.load("./sprites/message.png")
home_screen_rect = home_screen_img.get_rect(center=(175, 350))
transformedSky = pg.transform.scale(sky, (400, 711.11))
transformedGround = pg.transform.scale(ground, (400, 133.33))
gameOver = pg.image.load("./sprites/gameover.png")

# Sounds
flap_sound = pg.mixer.Sound("audio/wing.wav")
hit_sound = pg.mixer.Sound("audio/hit.wav")
point_sound = pg.mixer.Sound("audio/point.wav")
point_sound.set_volume(0.5)

# Groups
bird = pg.sprite.GroupSingle()
bird.add(Bird.birdClass())

pipe = pg.sprite.Group()
pipeSpawn = 0
pipePassed = False

score = 0
score_group = pg.sprite.Group()

# High Score Handling
def load_high_score():
    if os.path.exists("high_score.txt"):
        with open("high_score.txt", "r") as f:
            try:
                return int(f.read().strip())
            except:
                return 0
    return 0

def save_high_score(score):
    with open("high_score.txt", "w") as f:
        f.write(str(score))

highest_score = load_high_score()

# Font for displaying score text
font_score = pg.font.SysFont("Arial", 24)

def home_screen():
    global start
    while start:
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        screen.blit(transformedGround, (0, 570))
        screen.blit(home_screen_img, home_screen_rect)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    flap_sound.play()
                    start = False

def draw_highest_score_image(highest_score, surface, pos_x, pos_y):
    score_str = str(highest_score)
    digit_sprites = []
    for i, digit_char in enumerate(reversed(score_str)):
        digit = int(digit_char)
        digit_sprite = Score.scoreClass(i)
        digit_sprite.update(digit)
        digit_sprite.rect.midtop = (pos_x - 26 * i, pos_y)
        digit_sprites.append(digit_sprite)
    for digit_sprite in digit_sprites:
        screen.blit(digit_sprite.image, digit_sprite.rect)

def reset_game():
    global score, pipePassed, pipeSpawn, restart, start
    score = 0
    pipePassed = False
    pipeSpawn = 0
    pipe.empty()
    bird.empty()
    bird.add(Bird.birdClass())
    score_group.empty()
    start = True
    restart = True

def collision():
    global highest_score

    # Update high score if beaten BEFORE showing game over screen
    if score > highest_score:
        highest_score = score
        save_high_score(highest_score)

    if pg.sprite.spritecollide(bird.sprite, pipe, True):
        hit_sound.play()
        global restart
        restart = False

        screen.fill(Black)

        font_reset = pg.font.SysFont(
            "./fonts/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf", 30
        )

        # Your Score text
        your_score_text = font_reset.render(f"Your Score: {score}", True, White)
        your_score_rect = your_score_text.get_rect(center=(180, 220))

        # High Score text
        high_score_text = font_reset.render(f"High Score: {highest_score}", True, White)
        high_score_rect = high_score_text.get_rect(center=(180, 260))

        text_surface_reset = font_reset.render("Press Enter To RESTART", False, White)
        text_rect_restart = text_surface_reset.get_rect(center=(180, 350))
        gameOver_rect = gameOver.get_rect(center=(180, 300))

        screen.blit(your_score_text, your_score_rect)
        screen.blit(high_score_text, high_score_rect)
        screen.blit(gameOver, gameOver_rect)
        screen.blit(text_surface_reset, text_rect_restart)
        pg.display.flip()

        while True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
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

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_SPACE:
            flap_sound.play()

    screen.blit(transformedSky, (x1, 0))
    screen.blit(transformedSky, (x2, 0))

    transformedSky.blit(transformedGround, (x1, 570))
    transformedSky.blit(transformedGround, (x2, 570))

    home_screen()

    x1 -= 2
    if x1 < -20:
        x2 = x1 + 400
    x2 -= 2
    if x2 < -20:
        x1 = x2 + 400

    if pipeSpawn == 0:
        pipe.add(Pipes.pipeClass("Down"))
        pipe.add(Pipes.pipeClass("Up"))
    elif pipeSpawn >= 5:
        pipeSpawn = -0.1
    pipeSpawn += 0.1

    bird.draw(screen)
    check_collision = bird.update()
    if not check_collision:
        collision()
    pipe.draw(screen)
    pipe.update()
    temp = score

    for i in range(0, len(str(score))):
        score_group.add(Score.scoreClass(i))
        rem = temp % 10
        temp = int(temp / 10)
        score_group.sprites()[i].update(rem)

    collision()
    for i in pipe:
        if (
            not pipePassed
            and i.rect.left < bird.sprites()[0].rect.left
            and i.rect.right > bird.sprites()[0].rect.right
        ):
            pipePassed = True
        if pipePassed and i.rect.right < bird.sprites()[0].rect.left:
            pipePassed = False
            score += 1
            point_sound.play()

    # DRAW text-based High Score and Current Score
    high_text = font_score.render(f"High Score: {highest_score}", True, White)
    current_text = font_score.render(f"Score: {score}", True, White)
    screen.blit(high_text, (10, 10))          # Top-left corner
    screen.blit(current_text, (210, 10))      # Top-right corner

    score_group.draw(screen)
    pg.display.update()
    clock.tick(60)
