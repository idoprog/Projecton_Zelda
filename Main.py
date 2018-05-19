import pygame
import ctypes
pygame.init()
user32 = ctypes.windll.user32
width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
if width > 1280:
    width = 1280
if height > 720:
    height = 720
screen = pygame.display.set_mode((width, height), pygame.NOFRAME | pygame.FULLSCREEN, 32)
char_steps = 5

main_group = pygame.sprite.Group()
orc_group = pygame.sprite.Group()

class Sprite(pygame.sprite.Sprite):
    def __init__(self, screen_pos_x, screen_pos_y, board_pos_x, board_pos_y, char_width, char_height):
        super(Sprite, self).__init__()
        self.screen_pos = pygame.Rect(screen_pos_x, screen_pos_y, char_width, char_height)
        self.board_pos = pygame.Rect(board_pos_x, board_pos_y, char_width, char_height)
        self.direction = None

    @staticmethod
    def image_bliting(image_loc, pos_x, pos_y, angle):
        screen.blit(pygame.transform.rotate(pygame.image.load(image_loc), angle), (pos_x, pos_y))

    def calc_angle(self):
        if self.direction == 1:
            return 0
        elif self.direction == 2:
            return 270
        elif self.direction == 3:
            return 180
        else:
            return 90


class main_character(Sprite):
    def __init__(self, start_x, start_y):
        super(main_character, self).__init__(start_x, start_y, start_x + 1000, start_y + 1000, 81, 80)  # going to the father of rpg_board (pygame.Rect())
        self.direction = 1
        self.moving_seq = 1
        self.add(main_group)
        self.dirty = 2

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            board.move_up()
        elif keys[pygame.K_s]:
            board.move_down()
        elif keys[pygame.K_a]:
            board.move_left()
        elif keys[pygame.K_d]:
            board.move_right()
        else:
            board.char.breath()

    def breath(self):
        board.blit_board()
        state = False
        while True:
            if state:
                self.image_bliting('Textures/Skins/Main_Char/Animation/B/B1.png', self.screen_pos.left, self.screen_pos.top, self.calc_angle())
                state = False
            else:
                self.image_bliting('Textures/Skins/Main_Char/Animation/B/B2.png', self.screen_pos.left, self.screen_pos.top, self.calc_angle())
                state = True
            pygame.display.update()
            for x in range(1000):
                pygame.time.delay(1)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        return

    def walk(self, d):
        if self.direction == d:
            self.image_bliting('Textures\Skins\Main_Char\Animation\W\W' + str(self.moving_seq) + '.png', self.screen_pos.left, self.screen_pos.top, self.calc_angle())
        else:
            self.moving_seq = 1
            self.direction = d
            self.image_bliting('Textures\Skins\Main_Char\Animation\W\W1.png', self.screen_pos.left, self.screen_pos.top, self.calc_angle())
        self.moving_seq = self.moving_seq + 1
        if self.moving_seq == 35:
            self.moving_seq = 1
        for x in range(20):
            pygame.time.delay(1)
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    return


class Barriers(object):
    def __init__(self):
        self.walls_arr = []
        self.misc_arr = []
        self.enemy_arr = []
        self.wall_arr_init()
        self.misc_arr_init()

    def wall_arr_init(self):
        # walls adding, numbers according to the wall mapping picture
        # wall 1
        self.walls_arr.append(pygame.Rect(1000, 1180, 129, 2719))
        # wall 2
        self.walls_arr.append(pygame.Rect(1130, 1000, 7799, 179))
        # wall 3A
        self.walls_arr.append(pygame.Rect(8930, 1180, 66, 1249))
        # wall 3B
        self.walls_arr.append(pygame.Rect(8930, 2820, 66, 1079))
        # wall 4
        self.walls_arr.append(pygame.Rect(1130, 3900, 7799, 99))
        # wall 5
        self.walls_arr.append(pygame.Rect(5630, 1180, 89, 499))
        # wall 6
        self.walls_arr.append(pygame.Rect(3540, 1500, 2089, 179))
        # wall 7
        self.walls_arr.append(pygame.Rect(3430, 1500, 99, 499))
        # wall 8
        self.walls_arr.append(pygame.Rect(2630, 1180, 89, 819))
        # wall 9
        self.walls_arr.append(pygame.Rect(1130, 1930, 869, 89))
        # wall 10
        self.walls_arr.append(pygame.Rect(1820, 1180, 109, 319))
        # wall 11
        self.walls_arr.append(pygame.Rect(6220, 1180, 99, 889))
        # wall 12
        self.walls_arr.append(pygame.Rect(4110, 1930, 2109, 139))
        # wall 13
        self.walls_arr.append(pygame.Rect(7220, 1180, 99, 889))
        # wall 14
        self.walls_arr.append(pygame.Rect(7720, 1431, 1209, 138))
        # wall 15
        self.walls_arr.append(pygame.Rect(8000, 1820, 900, 149))
        # wall 16
        self.walls_arr.append(pygame.Rect(8000, 1970, 129, 99))
        # wall 17
        self.walls_arr.append(pygame.Rect(8220, 2320, 709, 109))
        # wall 18
        self.walls_arr.append(pygame.Rect(8220, 2820, 709, 149))
        # wall 19
        self.walls_arr.append(pygame.Rect(7820, 3220, 109, 679))
        # wall 20
        self.walls_arr.append(pygame.Rect(5320, 3220, 1998, 159))
        # wall 21
        self.walls_arr.append(pygame.Rect(5320, 3380, 109, 519))
        # wall 22
        self.walls_arr.append(pygame.Rect(4630, 3220, 109, 679))
        # wall 23
        self.walls_arr.append(pygame.Rect(3610, 3220, 109, 679))
        # wall 24
        self.walls_arr.append(pygame.Rect(2320, 3220, 899, 159))
        # wall 25
        self.walls_arr.append(pygame.Rect(2320, 3380, 109, 519))
        # wall 26
        self.walls_arr.append(pygame.Rect(1130, 3220, 869, 99))
        # wall 27: Door
        self.walls_arr.append(pygame.Rect(8930, 2430, 66, 389))

    def misc_arr_init(self):
        # misc 1: Rock
        self.misc_arr.append(pygame.Rect(1130, 1179, 200, 181))
        # misc 2: Rock
        self.misc_arr.append(pygame.Rect(1130, 1369, 60, 91))
        # misc 3: Rock
        self.misc_arr.append(pygame.Rect(1130, 2299, 100, 291))
        # misc 4: Rock
        self.misc_arr.append(pygame.Rect(1130, 2989, 100, 191))
        # misc 5: Rock
        self.misc_arr.append(pygame.Rect(2079, 3719, 240, 180))
        # misc 6: Rock
        self.misc_arr.append(pygame.Rect(3359, 3759, 250, 140))
        # misc 7: Rock
        self.misc_arr.append(pygame.Rect(3720, 3500, 190, 399))
        # misc 8: Rock
        self.misc_arr.append(pygame.Rect(5430, 3749, 130, 150))
        # misc 9: Rock
        self.misc_arr.append(pygame.Rect(7519, 3629, 271, 182))
        # misc 10: Rock
        self.misc_arr.append(pygame.Rect(7369, 3779, 450, 120))
        # misc 11: Rock
        self.misc_arr.append(pygame.Rect(7930, 3819, 30, 80))
        # misc 12: Rock
        self.misc_arr.append(pygame.Rect(8660, 3709, 269, 190))
        # misc 13: Rock
        self.misc_arr.append(pygame.Rect(8749, 1570, 180, 140))
        # misc 14: Rock
        self.misc_arr.append(pygame.Rect(8609, 1570, 61, 40))
        # misc 15: Rock
        self.misc_arr.append(pygame.Rect(7049, 1180, 121, 140))
        # misc 16: Rock
        self.misc_arr.append(pygame.Rect(6099, 2149, 141, 101))
        # misc 17: Rock
        self.misc_arr.append(pygame.Rect(6249, 2089, 141, 101))
        # misc 18: Rock
        self.misc_arr.append(pygame.Rect(4029, 2079, 161, 81))
        # misc 19: Rock
        self.misc_arr.append(pygame.Rect(4249, 2079, 121, 71))
        # misc 20: Rock
        self.misc_arr.append(pygame.Rect(2559, 2789, 141, 111))
        # misc 21: Rock
        self.misc_arr.append(pygame.Rect(2709, 2649, 261, 171))
        # misc 22: Rock
        self.misc_arr.append(pygame.Rect(6609, 3059, 431, 121))
        # misc 23: Rock + Webs
        self.misc_arr.append(pygame.Rect(2720, 1179, 80, 141))
        # misc 24: Statue
        self.misc_arr.append(pygame.Rect(4409, 2460, 701, 340))

    def can_pass_up(self, sprite, steps):
        for x in xrange(steps):
            sprite.board_pos.top -= 1
            if sprite.board_pos.collidelist(self.walls_arr) != -1 or sprite.board_pos.collidelist(self.misc_arr) != -1:
                sprite.board_pos.top += 1
                return x
        return steps

    def can_pass_down(self, sprite, steps):
        for x in xrange(steps):
            sprite.board_pos.top += 1
            if sprite.board_pos.collidelist(self.walls_arr) != -1 or sprite.board_pos.collidelist(self.misc_arr) != -1:
                sprite.board_pos.top -= 1
                return x
        return steps

    def can_pass_right(self, sprite, steps):
        for x in xrange(steps):
            sprite.board_pos.left += 1
            if sprite.board_pos.collidelist(self.walls_arr) != -1 or sprite.board_pos.collidelist(self.misc_arr) != -1:
                sprite.board_pos.left -= 1
                return x
        return steps

    def can_pass_left(self, sprite, steps):
        for x in xrange(steps):
            sprite.board_pos.left -= 1
            if sprite.board_pos.collidelist(self.walls_arr) != -1 or sprite.board_pos.collidelist(self.misc_arr) != -1:
                sprite.board_pos.left += 1
                return x
        return steps

class rpg_board(pygame.Rect):
    def __init__(self, start_x=0, start_y=0):
        super(rpg_board, self).__init__(start_x, start_y, start_x + width, start_y + height)
        self.image = pygame.image.load('Textures/Board/3/Board3.png').convert()
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        screen.blit(self.image, (0, 0), area=(self.left, self.top, self.width, self.height))
        pygame.display.update()
        self.Barriers = Barriers()
        self.char = main_character(width / 2, height / 2)

    def blit_board(self):
        screen.fill((255, 255, 255))
        screen.blit(self.image, (0, 0), area=(self.left, self.top, self.width, self.height))

    def move_up(self):
        real_step = self.Barriers.can_pass_up(self.char, char_steps)
        if real_step == 0:
            self.char.direction = 1
            self.char.breath()
            return
        self.top = self.top - real_step
        self.blit_board()
        self.char.walk(1)
        pygame.display.update()

    def move_down(self):
        real_step = self.Barriers.can_pass_down(self.char, char_steps)
        if real_step == 0:
            self.char.direction = 3
            self.char.breath()
            return
        self.top = self.top + real_step
        self.blit_board()
        self.char.walk(3)
        pygame.display.update()

    def move_left(self):
        real_step = self.Barriers.can_pass_left(self.char, char_steps)
        if real_step == 0:
            self.char.direction = 4
            self.char.breath()
            return
        self.left = self.left - real_step
        self.blit_board()
        self.char.walk(4)
        pygame.display.update()

    def move_right(self):
        real_step = self.Barriers.can_pass_right(self.char, char_steps)
        if real_step == 0:
            self.char.direction = 2
            self.char.breath()
            return
        self.left = self.left + real_step
        self.blit_board()
        self.char.walk(2)
        pygame.display.update()


board = rpg_board(1000, 1000)
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    board.char.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        finish = True

pygame.quit()
