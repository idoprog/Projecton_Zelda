import pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.NOFRAME | pygame.FULLSCREEN, 16)

img = pygame.Surface.convert(pygame.image.load('level5.png'))
img.set_clip(pygame.Rect(0, 0, 144, 81))
printer = img.subsurface(img.get_clip())
pygame.transform.scale(printer, (1920, 1080), screen)
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




