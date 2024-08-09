##############################################################################
#tictactoe.py
#Alex Wilmes
#7/23/2024
##############################################################################

import pygame as pg
import time

#Tile class takes image file names as str with position and size
class Tile(pg.sprite.Sprite): 
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
            
    def update(self, turn): #changes tile sprite 0
        if self.clicked == False:
            if turn % 2 == 0 and self.clicked == False: 
                self.clicked = True
                self.image = self.image_o
                self.letter = 'o'
            else:
                self.clicked = True
                self.image = self.image
                self.letter = 'x'
                
#class for winscreen
class WinScreen(pg.sprite.Sprite):
    #initializes win screen dimensions and position.
    def __init__(self, winner, position):
        super().__init__()
        self.size = (800, 800)
        self.image = pg.image.load('bluewinscreen.png')
        self.image = pg.transform.scale(self.image, self.size)
        self.winner = winner
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        
def check_win(tiles, turns):
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
          
def end_game(check_win): #function to end game
    if check_win() == 'x wins' or 'o wins':
        return False
    
def main():
    
    pg.init() #initializes pygame, creates window and background.
    window_size = (800, 800)
    screen = pg.display.set_mode(window_size)
    pg.display.set_caption('Tic Tac Toe')
    background_image = pg.image.load('background.png')
    
    #creates sprites and Group of sprites.
    sprite_size = ((800/24) * 6.5, (800/24) * 6.5)
       
    #initializing sprites and group #see if you can shorten this by the initializing value
    all_sprites = pg.sprite.Group()
    t1 = Tile('TicTacToeX.png', 'TicTacToeO.png', (35, 35), sprite_size)
    t2 = Tile('TicTacToeX.png', 'TicTacToeO.png', (290, 35), sprite_size)
    t3 = Tile('TicTacToeX.png', 'TicTacToeO.png', (547, 35), sprite_size)
    t4 = Tile('TicTacToeX.png', 'TicTacToeO.png', (35, 290), sprite_size)
    t5 = Tile('TicTacToeX.png', 'TicTacToeO.png', (290, 290), sprite_size)
    t6 = Tile('TicTacToeX.png', 'TicTacToeO.png', (547, 290), sprite_size)
    t7 = Tile('TicTacToeX.png', 'TicTacToeO.png', (35, 547), sprite_size)
    t8 = Tile('TicTacToeX.png', 'TicTacToeO.png', (290, 547), sprite_size)
    t9 = Tile('TicTacToeX.png', 'TicTacToeO.png', (547, 547), sprite_size)
    
    tiles = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    

    gameover = False
    turn = 0
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN: #Checks to see if sprite is clicked and shows if it is.
                mouse_pos = event.pos 
                if t1.rect.collidepoint(mouse_pos):
                    if t1.clicked == False:
                        all_sprites.add(t1)
                        turn += 1
                        t1.update(turn)
                        tiles[0] = t1.letter
                        print(tiles)
                        break
                elif t2.rect.collidepoint(mouse_pos):
                    if t2.clicked == False:
                        all_sprites.add(t2)
                        turn += 1
                        t2.update(turn)
                        tiles[1] = t2.letter
                        print(tiles)
                        break
                elif t3.rect.collidepoint(mouse_pos):
                    if t3.clicked == False:
                        all_sprites.add(t3)
                        turn += 1
                        t3.update(turn)
                        tiles[2] = t3.letter
                        print(tiles)
                        break
                elif t4.rect.collidepoint(mouse_pos):
                    if t4.clicked == False:
                        all_sprites.add(t4)
                        turn += 1
                        t4.update(turn)
                        tiles[3] = t4.letter
                        print(tiles)
                        break
                elif t5.rect.collidepoint(mouse_pos):
                    if t5.clicked == False:
                        all_sprites.add(t5)
                        turn += 1
                        t5.update(turn)
                        tiles[4] = t5.letter
                        print(tiles)
                        break
                elif t6.rect.collidepoint(mouse_pos):
                    if t6.clicked == False:
                        all_sprites.add(t6) 
                        turn += 1
                        t6.update(turn)
                        tiles[5] = t6.letter
                        print(tiles)
                        break
                elif t7.rect.collidepoint(mouse_pos):
                    if t7.clicked == False:
                        all_sprites.add(t7)
                        turn += 1
                        t7.update(turn)
                        tiles[6] = t7.letter
                        print(tiles)
                        break 
                elif t8.rect.collidepoint(mouse_pos):
                    if t8.clicked == False:
                        all_sprites.add(t8)
                        turn += 1
                        t8.update(turn)
                        tiles[7] = t8.letter
                        print(tiles)
                        break
                elif t9.rect.collidepoint(mouse_pos):
                    if t9.clicked == False:
                        all_sprites.add(t9)
                        turn += 1
                        t9.update(turn)
                        tiles[8] = t9.letter
                        print(tiles)
                        break
        
        #updates screen        
        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)
        pg.display.flip()
        
        #displays win screen
        check_win_var = check_win(tiles, turn)
        if check_win_var != 'play':
            pg.quit()
           
        
            

            
    

if __name__ == "__main__":
    main()
    