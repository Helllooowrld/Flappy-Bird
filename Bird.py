import pygame as pg


class birdClass(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bird1 = pg.image.load("./sprites/yellowbird-upflap.png")
        self.bird2 = pg.image.load("./sprites/yellowbird-midflap.png")
        self.bird3 = pg.image.load("./sprites/yellowbird-downflap.png")
        self.birdList = [self.bird1, self.bird2, self.bird3]
        self.birdIndex = 0
        self.image = self.birdList[self.birdIndex]
        self.rect = self.image.get_rect(center=(100, 350))
        self.gravity = 0
        self.flag = False


    def animation(self):
        self.birdIndex += 0.15
        self.image = self.birdList[int(self.birdIndex)]
        if self.birdIndex >= 2:
            self.birdIndex = 0

    def player_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.flag = True
            self.gravity = -4
            self.image = pg.transform.rotate(self.birdList[int(self.birdIndex)], 20)
            
    def apply_gravity(self):
        if self.flag:
            self.gravity += 0.5
            self.rect.y += self.gravity
            if self.gravity > 8:
                self.gravity = 8
            self.image = pg.transform.rotate(self.birdList[int(self.birdIndex)], 0)
            if self.rect.bottom >= 601:
                self.rect.y = 560
                return False
                

    def update(self):
        self.animation()
        self.apply_gravity()
        self.player_input()
