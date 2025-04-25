import pygame as pg


class birdClass(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bird1=pg.image.load('./sprites/redbird-upflap.png')
        self.bird2=pg.image.load('./sprites/redbird-midflap.png')
        self.bird3=pg.image.load('./sprites/redbird-downflap.png')
        self.birdList=[self.bird1,self.bird2,self.bird3]
        self.birdIndex=0
        self.image=self.birdList[self.birdIndex]
        self.rect=self.image.get_rect(center=(100,350))
        self.gravity=0
    
    def animation(self):
        self.birdIndex+=.15
        self.image=self.birdList[int(self.birdIndex)]
        if self.birdIndex>=2: self.birdIndex=0
    
    def player_input(self):
        keys=pg.key.get_pressed()
        if keys[pg.K_SPACE]:
           self.gravity=-15
    
    def apply_gravity(self):
        self.gravity+=1
        self.rect.y+=self.gravity
        if self.rect.bottom>=601:
            print("Game Over")
            self.rect.y=350
            pg.quit()
            
    def update(self):
        self.animation()
        self.apply_gravity()
        self.player_input()