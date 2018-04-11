import pygame
pygame.init()


screen = pygame.display.set_mode((1280, 720), pygame.NOFRAME | pygame.FULLSCREEN, 32)
steps = 5

class rpg_board(pygame.Rect):
    def __init__(self, start_x=0, start_y=0):
        super(rpg_board, self).__init__(start_x, start_y, start_x + 1280, start_y + 720)
        self.image = pygame.image.load('Textures/Board/3/Board3.png').convert()
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        screen.blit(self.image, (0, 0), area=(self.left, self.top, self.width, self.height))
        pygame.display.update()

    def blit_board(self):
        screen.fill((255, 255, 255))
        screen.blit(self.image, (0, 0), area=(self.left, self.top, self.width, self.height))

    def move_up(self, steps):
        if self.top - steps == 0:
            return
        self.top = self.top - steps
        self.height = self.height - steps
        self.blit_board()
        char.walk(1)
        pygame.display.update()

    def move_down(self, steps):
        if self.height + steps == self.image_height:
            return
        self.height = self.height + steps
        self.top = self.top + steps
        self.blit_board()
        char.walk(3)
        pygame.display.update()

    def move_left(self, steps):
        if self.left - steps == 0:
            return
        self.left = self.left - steps
        self.width = self.width - steps
        self.blit_board()
        char.walk(4)
        pygame.display.update()

    def move_right(self, steps):
        if self.width + steps == self.image_width:
            return
        self.width = self.width + steps
        self.left = self.left + steps
        self.blit_board()
        char.walk(2)
        pygame.display.update()


board = rpg_board(130, 920)


class main_character(rpg_board):
    def __init__(self, start_x, start_y):
        super(rpg_board, self).__init__(start_x, start_y, start_x + 80, start_y + 80)  #going to the father of rpg_board (pygame.Rect())
        self.direction = 1
        self.moving_seq = 1
    @staticmethod
    def image_bliting(image_loc, pos_x, pos_y, angle):
        screen.blit(pygame.transform.rotate(pygame.image.load(image_loc), angle),(pos_x, pos_y))

    def calc_angle(self):
        if self.direction == 1:
            return 0
        elif self.direction == 2:
            return 270
        elif self.direction == 3:
            return 180
        else:
            return 90

    def breath(self):
        board.blit_board()
        state = False
        while True:
            if state:
                self.image_bliting('Textures/Skins/Main_Char/Animation/B/B1.png', self.left, self.top, self.calc_angle())
                state = False
            else:
                self.image_bliting('Textures/Skins/Main_Char/Animation/B/B2.png', self.left, self.top, self.calc_angle())
                state = True
            pygame.display.update()
            for x in range(1000):
                pygame.time.delay(1)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        return

    def walk(self, d):
        if self.direction == d:
            self.image_bliting('Textures\Skins\Main_Char\Animation\W\W' + str(self.moving_seq) + '.png', self.left, self.top, self.calc_angle())
        else:
            self.moving_seq = 1
            self.direction = d
            self.image_bliting('Textures\Skins\Main_Char\Animation\W\W1.png', self.left, self.top, self.calc_angle())
        self.moving_seq = self.moving_seq + 1
        if self.moving_seq == 35:
            self.moving_seq = 1
        for x in range(20):
            pygame.time.delay(1)
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    return


char = main_character(600, 320)


finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        finish = True
    if keys[pygame.K_w]:
        board.move_up(steps)
    elif keys[pygame.K_s]:
        board.move_down(steps)
    elif keys[pygame.K_a]:
        board.move_left(steps)
    elif keys[pygame.K_d]:
        board.move_right(steps)
    else:
        char.breath()


pygame.quit()
