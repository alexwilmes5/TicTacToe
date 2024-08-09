#tile.py
#class for tile sprite

import pygame as pg

class Tile(pg.sprite.Sprite): #initializes tile class with images, position and size
    def __init__(self, image_path_x, image_path_o, position, size):
        super().__init__()
        self.image = pg.image.load(image_path_x)
        self.image = pg.transform.scale(self.image, size)
        self.image_o = pg.image.load(image_path_o)
        self.image_o = pg.transform.scale(self.image_o, size)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.letter = None
        self.clicked = False
        self.turn = 0
              
    def update(self, turn): #updates tile and attributes when clicked
        if self.clicked == False:
            if self.turn % 2 == 0 and self.clicked == False: 
                self.clicked = True
                self.image = self.image_o
                self.letter = 'o'
                
            else:
                self.clicked = True
                self.image = self.image
                self.letter = 'x'
                

        
    


