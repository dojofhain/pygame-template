import pygame


class Game(object):

    def __init__(self, width=800, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.fonts = {}

    def update(self):
        pass

    def keys_pressed(self, keys):
        pass

    def draw_image(self, image):
        int_position = (int(image.x), int(image.y))
        self.screen.blit(image.img, dest=int_position)

    def draw_rect(self, rect, color=(255, 255, 255)):
        self.screen.fill(color, rect)

    def draw_circle(self, position, color=(255, 255, 255), radius=0):
        int_position = (int(position[0]), int(position[1]))
        pygame.draw.circle(self.screen, color, int_position, radius)

    def draw_text(self, text, position=(0, 0), color=(255, 255, 255), size=25):
        int_position = (int(position[0]), int(position[1]))
        font = self.__get_font(size)
        self.screen.blit(font.render(text, True, color), int_position)

    def start(self):
        keep_going = True
        while keep_going:
            keys = pygame.key.get_pressed()
            self.keys_pressed(keys)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keep_going = False

            self.screen.fill((0, 0, 0))
            self.update()
            pygame.display.flip()

    def __get_font(self, size):
        font = self.fonts.get(size)
        if not font:
            font = pygame.font.SysFont('Arial', size)
            self.fonts[size] = font
        return font
