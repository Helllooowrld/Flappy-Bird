import pygame as pg
from sys import exit



class scoreClass(pg.sprite.Sprite):
    def __init__(self,len):
        super().__init__()
        a = pg.image.load("./sprites/0.png").convert_alpha()
        b = pg.transform.scale((pg.image.load("./sprites/1.png")).convert_alpha(), (24, 36))
        c = pg.image.load("./sprites/2.png").convert_alpha()
        d = pg.image.load("./sprites/3.png").convert_alpha()
        e = pg.image.load("./sprites/4.png").convert_alpha()
        f = pg.image.load("./sprites/5.png").convert_alpha()
        g = pg.image.load("./sprites/6.png").convert_alpha()
        h = pg.image.load("./sprites/7.png").convert_alpha()
        i = pg.image.load("./sprites/8.png").convert_alpha()
        j = pg.image.load("./sprites/9.png").convert_alpha()
        self.scoreList = [a, b, c, d, e, f, g, h, i, j]
        self.image=b
        self.x=0
        self.rect=self.image.get_rect(midtop=(175-26*len,0))

    
    
    def update(self,score):
        self.image=self.scoreList[score]
   
      
        
        
       
      


