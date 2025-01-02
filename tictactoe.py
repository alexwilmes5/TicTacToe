##############################################################################
#tictactoe.py
#Alex Wilmes
#7/23/2024
##############################################################################

#pygame module needed for program to work
import pygame as pg

class Tile(pg.sprite.Sprite): #initializes tile class with images, position, index_num, 
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
            
    def get_index(self): #returns index number of tile to proper update tiles list
        return self.index_num
     
def check_win(tiles, turns): #determines if players have won, lost or tied.
    winning_positions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), #rows left to right
                        (0, 3, 6), (1, 4, 7), (2, 5, 8), #rows up and down
                        (0, 4, 8), (2, 4, 6)) #rows diagonally
    
    for win_pos in winning_positions: #iterates over each tile and checks to see if player has won   
        if tiles[win_pos[0]] == tiles[win_pos[1]] == tiles[win_pos[2]] and tiles[win_pos[0]] != 0:
            if tiles[win_pos[0]] == 'x':
                return 'x wins'
            elif tiles[win_pos[0]] == 'o':
                return 'o wins'
        elif turns == 9: 
            return 'no winner'
     
#func to display game ending screen once game is finished. 
def display_end_screen(screen, end_image):
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                return
        screen.blit(end_image, (0, 0))
        pg.display.flip()
        pg.time.wait(100)
 
#determines which end screen to display        
def determine_endscreen(check_win_var, screen, redwinscreen, bluewinscreen, no_winner_screen, turn):
    if check_win_var == 'o wins':
        pg.time.wait(1000)
        display_end_screen(screen, redwinscreen)
    elif check_win_var == 'x wins':
        pg.time.wait(1000)
        display_end_screen(screen, bluewinscreen)
    elif turn == 9:
        pg.time.wait(1000)
        display_end_screen(screen, no_winner_screen)
    else:
        return
                
def play_sound(turn, x_sound, o_sound): #plays sound when player clicks
    if turn % 2 == 0: #the sound that is played is determined by players turn
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
    redwinscreen = pg.image.load('assets/redwinscreen.png')
    no_winner_screen = pg.image.load('assets/nowinnerscreen.png')
    
    #loads and plays music
    pg.mixer.music.load('assets/tictactoe_music.mp3')
    pg.mixer.music.play(-1)
    
    #creates variables for click sounds
    x_sound = pg.mixer.Sound('assets/x_sound.mp3')
    o_sound = pg.mixer.Sound('assets/o_sound.mp3')
    
    #creates sprites and Group of sprites.
    sprite_size = ((800/24) * 6.6, (800/24) * 6.6)
       
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
    tiles = [0] * 9 

    #sprites are put into list to be easily accessed later
    sprite_list = [t1, t2, t3, t4, t5, t6, t7, t8, t9]
    
    #turn and running are initialized to start program and have proper X and O drawing
    turn = 0
    running = True
    
    while running: #closes window if player exits program
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                
            elif event.type == pg.MOUSEBUTTONDOWN: #Checks to see if sprite is clicked and shows if it is.
                mouse_pos = event.pos 
                #constantly iterating over all sprites and seeing if they need to be updated
                for sprite in sprite_list:
                    if sprite.rect.collidepoint(mouse_pos):
                        if sprite.clicked == False:
                            all_sprites.add(sprite)
                            play_sound(turn, x_sound, o_sound)
                            turn += 1
                            sprite.update(turn)
                            tiles[sprite.get_index()] = sprite.letter
                            break
                        
        #updates screen 
        check_win_var = check_win(tiles, turn)       
        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)
        pg.display.flip()

        #outputs end screen
        determine_endscreen(check_win_var, screen, redwinscreen, bluewinscreen, no_winner_screen, turn)
             
if __name__ == "__main__":
    main()
    
    