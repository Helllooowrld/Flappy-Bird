import pygame as pg
import random


class pipeClass(pg.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.random=0

        if type == 'Down':
            self.fullImage = pg.image.load(
                "./sprites/pipe-green.png").convert_alpha()
            box = pg.Rect(0, 0, self.fullImage.get_width(), random.randint(100, 290))

            self.image = self.fullImage.subsurface(box)
            self.rect = self.image.get_rect(midbottom=(370, 570))
        else:
            self.fullImage = pg.image.load(
                "./sprites/pipe-red.png").convert_alpha()
            self.box = pg.Rect(0, 0, self.fullImage.get_width(), random.randint(100, 310))
            self.image = pg.transform.rotate(
                self.fullImage.subsurface(self.box), 180)
            self.rect = self.image.get_rect(midtop=(370,-60))

    def scroll(self):
        self.rect.x -= 4
        # self.random=

    def destroy(self):
        if self.rect.x < -100:
            self.kill()

    def update(self):
        self.scroll()
        self.destroy()
