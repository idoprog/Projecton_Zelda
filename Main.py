import pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.NOFRAME, 16)
pygame.display.toggle_fullscreen()

finish = False

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        finish = True
pygame.quit()




