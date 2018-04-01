import os

os.environ['SDL_VIDEO_WINDOW_POS'] = str(0) + "," + str(0)

import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720),pygame.NOFRAME,32)


class rpg_board(object):
    def __init__(self, screen, start_x=0, start_y=0):
        self.screen = screen
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = start_x + 1280
        self.end_y = start_y + 720
        self.image = pygame.image.load('Textures/Board/3/Board3.png').convert()
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        screen.blit(self.image, (0, 0), area=(0, 0, 1280, 720))
        pygame.display.update()

    def print_image(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.image, (0, 0), area=(self.start_x, self.start_y, self.end_x, self.end_y))
        pygame.display.update()

    def move_up(self):
        if self.start_y - 10 == 0:
            return
        self.start_y = self.start_y-10
        self.end_y = self.end_y -10
        self.print_image()

    def move_down(self):
        if self.end_y + 10 == self.image_height:
            return
        self.end_y = self.end_y + 10
        self.start_y = self.start_y + 10
        self.print_image()

    def move_left(self):
        if self.start_x - 10 == 0:
            return
        self.start_x = self.start_x - 10
        self.end_x = self.end_x - 10
        self.print_image()

    def move_right(self):
        if self.end_x + 10 == self.image_width:
            return
        self.end_x = self.end_x + 10
        self.start_x = self.start_x + 10
        self.print_image()




board = rpg_board(screen, 0, 0)
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

pygame.quit()
