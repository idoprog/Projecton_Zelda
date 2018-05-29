import pygame
pygame.init()


screen = pygame.display.set_mode((1280, 720), pygame.NOFRAME | pygame.FULLSCREEN, 32)
image = pygame.image.load('Textures\Skins\Main_Char\MC_S.png')
lol = pygame.display.get_surface()

sprite = pygame.sprite.Sprite()
print sprite
screen.blit(pygame.transform.rotate(image, 90), (100, 100))
screen.blit(pygame.transform.rotate(image, 180), (500, 500))
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
