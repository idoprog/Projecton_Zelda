import pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.NOFRAME | pygame.FULLSCREEN, 16)


class rpg_board(object):
    def __init__(self, screen, start_x=0, start_y=0):
        self.screen = screen
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = start_x + 1920
        self.end_y = start_y + 1080
        self.image = pygame.image.load('level5.png')
        self.image_width = pygame.self.image.get_size().get_width()
        self.image_height = pygame.self.image.get_size().get_height()
        screen.blit(self.image, (0, 0), area=(self.start_x, self.start_y, self.end_x, self.end_y))
        pygame.display.update()

    def print_image(self):
        screen.fill((255, 255, 255))
        screen.blit(self.image, (0, 0), area=(self.start_x, self.start_y, self.end_x, self.end_y))
        pygame.display.update()

    def move_up(self):
        self.start_y = self.start_y - 10
        self.end_y = self.end_y - 10
        self.print_image()

    def move_down(self):
        self.start_y = self.start_y + 10
        self.end_y = self.end_y + 10
        self.print_image()

    def move_left(self):
        self.start_x = self.start_x - 10
        self.end_x = self.end_x - 10
        self.print_image()

    def move_right(self):
        self.start_x = self.start_x + 10
        self.end_x = self.end_x + 10
        self.print_image()

    def is_edge(self, direction):
        if direction == 'up':
            if self.start_y == 0:
                return False
            else:
                return True
        elif direction == 'down':
            if self.end_y == self.image_height:



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
