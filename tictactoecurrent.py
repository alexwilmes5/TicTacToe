##############################################################################
#tictactoe.py
#Alex Wilmes
#7/23/2024
##############################################################################

import pygame as pg
import time

class Tile(pg.sprite.Sprite): #initializes tile class with images, position and size
    def __init__(self, image_path_x, image_path_o, position, size, index_num):
        super().__init__()
        self.image = pg.image.load(image_path_x)
        self.image = pg.transform.scale(self.image, size)
        self.image_o = pg.image.load(image_path_o)
        self.image_o = pg.transform.scale(self.image_o, size)
        self.index_num = index_num
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.letter = None
        self.clicked = False
              
    def update(self, turn): #updates tile and attributes when clicked
        if self.clicked == False and turn % 2 == 0:
                self.clicked = True
                self.image = self.image_o
                self.letter = 'o'
                
        else:
            self.clicked = True
            self.image = self.image
            self.letter = 'x'
            
    def get_index(self):
        return self.index_num
        
#Tile class takes image file names as str with position and size
     
def check_win(tiles, turns): #determines if players have won, lost or tied.
    
    #checks left to right across rows
    if tiles[0] == 'x' and tiles[1] == 'x' and tiles[2] == 'x':
        return 'x wins'
    if tiles[3] == 'x' and tiles[4] == 'x' and tiles[5] == 'x':
        return 'x wins'
    if tiles[6] == 'x' and tiles[7] == 'x' and tiles[8] == 'x':
        return 'x wins'
    if tiles[0] == 'o' and tiles[1] == 'o' and tiles[2] == 'o':
        return 'o wins'
    if tiles[3] == 'o' and tiles[4] == 'o' and tiles[5] == 'o':
        return 'o wins'
    if tiles[6] == 'o' and tiles[7] == 'o' and tiles[8] == 'o':
        return 'o wins'
    
    #checks up and down columns
    if tiles[0] == 'x' and tiles[3] == 'x' and tiles[6] == 'x':
        return 'x wins'
    if tiles[1] == 'x' and tiles[4] == 'x' and tiles[7] == 'x':
        return 'x wins'
    if tiles[2] == 'x' and tiles[5] == 'x' and tiles[8] == 'x':
        return 'x wins'
    if tiles[0] == 'o' and tiles[3] == 'o' and tiles[6] == 'o':
        return 'o wins'
    if tiles[1] == 'o' and tiles[4] == 'o' and tiles[7] == 'o':
        return 'o wins'
    if tiles[2] == 'o' and tiles[5] == 'o' and tiles[8] == 'o':
        return 'o wins'
    
    #checks diagonally
    if tiles[0] == 'x' and tiles[4] == 'x' and tiles[8] == 'x':
        return 'x wins'
    if tiles[2] == 'x' and tiles[4] == 'x' and tiles[6] == 'x':
        return 'x wins'
    if tiles[0] == 'o' and tiles[4] == 'o' and tiles[8] == 'o':
        return 'o wins'
    if tiles[2] == 'o' and tiles[4] == 'o' and tiles[6] == 'o':
        return 'o wins'
    
    #checks to see if nobody won
    elif turns == 9:
        return 'no winner'
    else: #string to indicate to keep playing
        return 'play'
          
#func to display game ending screen once game is finished. 
def end_screen(check_win_var, screen, bluewinscreen, redwinscreen, no_winner_screen, all_sprites): 
    if check_win_var == 'play': #does not display 
        return
    elif check_win_var == 'x wins':
        screen.blit(bluewinscreen, (0, 0))
        all_sprites.empty()
        pg.display.flip()
        time.sleep(4)
        pg.quit()
    elif check_win_var == 'o wins':
        screen.blit(redwinscreen, (0, 0))
        all_sprites.empty()
        pg.display.flip()
        time.sleep(4)
        pg.quit()
    elif check_win_var == 'no winner':
        screen.blit(no_winner_screen, (0, 0))
        all_sprites.empty()
        pg.display.flip()
        time.sleep(4)
        pg.quit()
        
def play_sound(turn, x_sound, o_sound):
    if turn % 2 == 0:
        o_sound.set_volume(1.5)
        o_sound.play()
    else:
        x_sound.set_volume(1.5)
        x_sound.play()
        
def main():
    pg.init() #initializes pygame, creates window, background and images used for win screen).
    pg.mixer.init() #initializes mixer for music
    window_size = (800, 800)
    screen = pg.display.set_mode(window_size)
    pg.display.set_caption('Tic Tac Toe')
    background_image = pg.image.load('assets/background.png')
    bluewinscreen = pg.image.load('assets/bluewinscreen.png')
    redwinscreen = pg.image.load('assets/redwinscreen.jpg')
    no_winner_screen = pg.image.load('assets/nowinnerscreen.jpg')
    
    #loads and plays music
    pg.mixer.music.load('assets/tictactoe_music.mp3')
    pg.mixer.music.play(-1)
    
    #creates variables for click sounds
    x_sound = pg.mixer.Sound('assets/x_sound.mp3')
    o_sound = pg.mixer.Sound('assets/o_sound.mp3')
    
    #creates sprites and Group of sprites.
    sprite_size = ((800/24) * 6.5, (800/24) * 6.5)
       
    #initializing sprites and group #see if you can shorten this by the initializing value
    all_sprites = pg.sprite.Group()
    t1 = Tile('assets/TicTacToeX.png', 'assets/TicTacToeO.png', (35, 35), sprite_size, 0)
    t2 = Tile('assets/TicTacToeX.png', 'assets/TicTacToeO.png', (290, 35), sprite_size, 1)
    t3 = Tile('assets/TicTacToeX.png', 'assets/TicTacToeO.png', (547, 35), sprite_size, 2)
    t4 = Tile('assets/TicTacToeX.png', 'assets/TicTacToeO.png', (35, 290), sprite_size, 3)
    t5 = Tile('assets/TicTacToeX.png', 'assets/TicTacToeO.png', (290, 290), sprite_size, 4)
    t6 = Tile('assets/TicTacToeX.png', 'assets/TicTacToeO.png', (547, 290), sprite_size, 5)
    t7 = Tile('assets/TicTacToeX.png', 'assets/TicTacToeO.png', (35, 547), sprite_size, 6)
    t8 = Tile('assets/TicTacToeX.png', 'assets/TicTacToeO.png', (290, 547), sprite_size, 7)
    t9 = Tile('assets/TicTacToeX.png', 'assets/TicTacToeO.png', (547, 547), sprite_size, 8)
    
    #array used for checking tic tac toe combinations
    tiles = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    sprite_list = [t1, t2, t3, t4, t5, t6, t7, t8, t9]
    
    turn = 0
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN: #Checks to see if sprite is clicked and shows if it is.
                mouse_pos = event.pos 
                for sprite in sprite_list:
                    if sprite.rect.collidepoint(mouse_pos):
                        if sprite.clicked == False:
                            all_sprites.add(sprite)
                            play_sound(turn, x_sound, o_sound)
                            turn += 1
                            sprite.update(turn)
                            tiles[sprite.get_index()] = sprite.letter
                            print(tiles)
                            break
                        
        #updates screen 
        check_win_var = check_win(tiles, turn)       
        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)
        pg.display.flip()
        
        if check_win_var != 'play': #creates delay to make final tile placement appear before end screen
            time.sleep(1)
        
        #outputs end screen
        end_screen(check_win_var, screen, bluewinscreen, redwinscreen, no_winner_screen, all_sprites)
       
  
if __name__ == "__main__":
    main()
    
    