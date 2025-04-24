import pygame as pg


class birdClass(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pg.image.load('./sprites/redbird-midflap.png')
        self.rect=self.image.get_rect(center=(100,350))
    
