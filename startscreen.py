##################################################################
#Class for start screen and start button
##################################################################

import pygame as pg
import time
                       
def load_screen(window_size):     
    pg.init()
    screen = pg.display.set_mode(window_size)
    pg.display.set_caption('Start Screen Test')
    background_image = pg.image.load('start_screen.png')
    screen.blit(background_image, (0, 0))
    pg.display.flip()
    return screen
    
class StartButton(pg.sprite.Sprite):
    def __init__(self, screen, window_size, size =(400, 200), position = (200, 400)):
        super().__init__()
        self.screen = screen
        self.image = pg.image.load('start_button.png')
        self.image = pg.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.visible = True
        self.rect.center = (window_size[0] // 2, window_size[1] // 1.8)
        
    def handle_click(self, event):      
        if self.rect.collidepoint(event.pos):
            print('Clicked')
            self.visible = False
            self.update() # Hide the sprite when clicked

    def update(self):
        if not self.visible:
            self.image.set_alpha(0)
            print('update method test')

            # Make the sprite invisible
       
        
def main():
    window_size = (800, 800)
    screen = load_screen(window_size)
    background = pg.image.load('start_screen.png').convert()
    start_button = StartButton(screen, window_size)
    sprite_group = pg.sprite.Group()
    sprite_group.add(start_button)
    
    
     # Position the button in the center
    
    running = True
    while running:
        event_list = pg.event.get()
        for event in event_list:
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                start_button.handle_click(event)
               
        sprite_group.update()
        screen.blit(background, (0, 0))
        sprite_group.draw(screen)       
        pg.display.flip()    

if __name__ == "__main__":
    main()