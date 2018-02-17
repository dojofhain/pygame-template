import pygame


class Image(object):

    def __init__(self, name):
        self.img = pygame.image.load(name)
        self.x = 0
        self.y = 0

    def width(self):
        return self.img.get_width()

    def height(self):
        return self.img.get_height()
