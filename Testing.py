import os

os.environ['SDL_VIDEO_WINDOW_POS'] = str(0) + "," + str(0)
import pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080))

image = pygame.image.load('Textures/Board/3/Board3.png')
screen.blit(image, (0, 0))
pygame.display.update()



finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        finish = True



pygame.quit()