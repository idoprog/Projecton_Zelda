import os

os.environ['SDL_VIDEO_WINDOW_POS'] = str(0) + "," + str(0)

import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720),pygame.NOFRAME,32)


class rpg_board(pygame.Rect):
    def __init__(self, start_x=0, start_y=0):
        super(rpg_board, self).__init__(start_x, start_y, start_x + 1280, start_y + 720)
        self.image = pygame.image.load('Textures/Board/3/Board3.png').convert()
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        screen.blit(self.image, (0, 0), area=(self.left, self.top, self.width, self.height))
        pygame.display.update()

    def blit_image(self):
        screen.fill((255, 255, 255))
        screen.blit(self.image, (0, 0), area=(self.left, self.top, self.width, self.height))


    def move_up(self):
        if self.top - 10 == 0:
            return
        self.top = self.top-10
        self.height = self.height -10
        self.blit_image()

    def move_down(self):
        if self.height + 10 == self.image_height:
            return
        self.height = self.height + 10
        self.top = self.top + 10
        self.blit_image()

    def move_left(self):
        if self.left - 10 == 0:
            return
        self.left = self.left - 10
        self.width = self.width - 10
        self.blit_image()

    def move_right(self):
        if self.width + 10 == self.image_width:
            return
        self.width = self.width + 10
        self.left = self.left + 10
        self.blit_image()


board = rpg_board(0, 0)


class main_character(rpg_board):
    def __init__(self,start_x, start_y):
        super(rpg_board, self).__init__(start_x, start_y, start_x + 80, start_y + 80)

    def image_bliting(self, image_loc, pos_x, pos_y):
        screen.blit(pygame.image.load(image_loc),(pos_x, pos_y))

    def breath(self, state):
        board.blit_image()
        if(state):
            self.image_bliting('Textures/Skins/Main_Char/Animation/B/B1.png', self.left, self.top)
            return False
        else:
            self.image_bliting('Textures/Skins/Main_Char/Animation/B/B2.png', self.left, self.top)
            return True

char = main_character(600,320)

state = True
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        finish = True
    if keys[pygame.K_w]:
        board.move_up()
    elif keys[pygame.K_s]:
        board.move_down()
    elif keys[pygame.K_a]:
        board.move_left()
    elif keys[pygame.K_d]:
        board.move_right()
    else:
        state = char.breath(state)

    pygame.display.update()
    pygame.time.delay(1000)
pygame.quit()
