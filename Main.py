import os

os.environ['SDL_VIDEO_WINDOW_POS'] = str(0) + "," + str(0)

import pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.NOFRAME)
global_step = 20

class rpg_board(object):
    def __init__(self, screen, start_x=0, start_y=0):
        self.screen = screen
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = start_x + 1920
        self.end_y = start_y + 1080
        self.image = pygame.image.load('Textures/Board/3/Board3.png').convert()
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        screen.blit(self.image, (0, 0), area=(self.start_x, self.start_y, self.end_x, self.end_y))
        pygame.display.update()

    def print_image(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.image, (0, 0), area=(self.start_x, self.start_y, self.end_x, self.end_y))
        pygame.display.update()

    def move_up(self, steps):
        if not self.is_edge('up'):
            return
        for x in range(steps):
            self.start_y = self.start_y - 1
            if not self.is_edge('up'):
                self.print_image()
                return
            if x == steps-1:
                self.start_y = self.start_y - 1
                self.end_y = self.end_y - steps
                self.print_image()
                return

    def move_down(self, steps):
        if not self.is_edge('down'):
            return
        for x in range(steps):
            self.end_y = self.end_y + 1
            if not self.is_edge('down'):
                self.print_image()
                return
            if x == steps-1:
                self.end_y = self.end_y + 1
                self.start_y = self.start_y + steps
                self.print_image()
                return

    def move_left(self, steps):
        if not self.is_edge('left'):
            return
        for x in range(steps):
            self.start_x = self.start_x - 1
            if not self.is_edge('left'):
                self.print_image()
                return
            if x == steps-1:
                self.start_x = self.start_x - 1
                self.end_x = self.end_x - steps
                self.print_image()
                return

    def move_right(self, steps):
        if not self.is_edge('right'):
            return
        for x in range(steps):
            self.end_x = self.end_x + 1
            if not self.is_edge('right'):
                self.print_image()
                return
            if x == steps-1:
                self.end_x = self.end_x + 1
                self.start_x = self.start_x + steps
                self.print_image()
                return

    def is_edge(self, direction):
        if direction == 'up':
            if self.start_y == 0:
                return False
            else:
                return True
        elif direction == 'down':
            if self.end_y == self.image_height:
                return False
            else:
                return True
        elif direction == 'right':
            if self.end_x == self.image_width:
                return False
            else:
                return True
        elif direction == 'left':
            if self.start_x == 0:
                return False
            else:
                return True


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
        board.move_up(global_step)
    elif keys[pygame.K_s]:
        board.move_down(global_step)
    elif keys[pygame.K_a]:
        board.move_left(global_step)
    elif keys[pygame.K_d]:
        board.move_right(global_step)

pygame.quit()
