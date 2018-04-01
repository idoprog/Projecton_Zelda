import pygame

class Entry(object):
    def __init__(self, starting_pos_x, starting_pos_y, size, screen):
        self.starting_pos_x = starting_pos_x
        self.starting_pos_y = starting_pos_y
        self.size = size
        self.ending = pygame.image.load('Textures\Text\Entry\Ending.png')
        self.body = pygame.image.load('Textures\Text\Entry\Body.png')



    def print_image(self, image, current_x, current_y):
        self.screen.blit(image, (current_x, current_y))
