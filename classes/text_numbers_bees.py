from os import path
import pygame
from classes import colors


class NumbersBees:
    def __init__(self, locator):
        size = int(0.65 * locator.block_size[0])
        position = (locator.shift_horizontal + locator.block_size[0] // 2 + int(2.5 * locator.block_size[0]),
                    locator.shift_vertical + locator.block_size[1] // 2 + int(1 * locator.block_size[1]))
        self.text = "КОЛИЧЕСТВО"
        self.color = colors.GREEN
        self.size = size
        self.position = position
        font_dir = path.join(path.dirname(__file__), '..')
        font_dir = path.join(font_dir, 'res')
        self.font = path.join(font_dir, "Adigiana_2.ttf")
        self.sized_font = pygame.font.Font(self.font, self.size)
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()

        self.is_activated = False

    def draw(self, surface):
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()
        self.rect.center = self.position
        surface.blit(self.render, self.rect)

    def update(self):
        pass
