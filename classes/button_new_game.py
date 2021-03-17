from os import path
import pygame
from classes import colors


class ButtonNewGame:
    def __init__(self, locator):
        size = int(1.5 * locator.block_size[0])
        position = (locator.width//2,
                    locator.shift_vertical + int(3 * locator.block_size[1]))
        self.text = "- НОВАЯ ИГРА -"
        self.main_color = colors.YELLOW
        self.activated_color = colors.GREEN
        self.current_color = self.main_color
        self.main_size = size
        self.position = position
        font_dir = path.join(path.dirname(__file__), '..')
        font_dir = path.join(font_dir, 'res')
        self.font = path.join(font_dir, "Adigiana_2.ttf")
        self.sized_font = pygame.font.Font(self.font, self.main_size)
        self.render = self.sized_font.render(self.text, True, self.current_color)
        self.rect = self.render.get_rect()

        self.is_activated = False

    def draw(self, surface):
        self.render = self.sized_font.render(self.text, True, self.current_color)
        self.rect = self.render.get_rect()
        self.rect.center = self.position
        surface.blit(self.render, self.rect)

    def update(self):
        # Активация при наведенин курсора
        mouse_cursor = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_cursor):
            self.current_color = self.activated_color
            self.sized_font = pygame.font.Font(self.font, int(self.main_size*1.2))
        else:
            self.current_color = self.main_color
            self.sized_font = pygame.font.Font(self.font, self.main_size)

        # Активность при клике
        self.is_activated = False
        if self.rect.collidepoint(mouse_cursor):
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:
                self.is_activated = True
