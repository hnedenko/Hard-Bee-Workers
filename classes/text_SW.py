from os import path
import pygame
from classes import colors
from main_classes import sound_player


class TextSW:
    def __init__(self, locator, saver, sound_player):
        self.saver = saver
        self.sound_player = sound_player
        self.is_active = False
        if saver.load_state()["sound_mode"] == "SW":
            self.is_active = True
        size = int(1 * locator.block_size[0])
        position = (locator.shift_horizontal + int(9 * locator.block_size[0])//2,
                    locator.shift_vertical + int(14 * locator.block_size[1]))
        self.text = "Star Wars"
        self.active_color = colors.ORANGE
        self.passive_color = colors.YELLOW
        self.under_mouse = colors.GREEN
        self.size = size
        self.position = position
        font_dir = path.join(path.dirname(__file__), '..')
        font_dir = path.join(font_dir, 'res')
        self.font = path.join(font_dir, "Adigiana_2.ttf")
        self.sized_font = pygame.font.Font(self.font, self.size)
        if self.is_active:
            self.current_color = self.active_color
        else:
            self.current_color = self.passive_color
        self.render = self.sized_font.render(self.text, True, self.current_color)
        self.rect = self.render.get_rect()

    def draw(self, surface):
        self.render = self.sized_font.render(self.text, True, self.current_color)
        self.rect = self.render.get_rect()
        self.rect.center = self.position
        surface.blit(self.render, self.rect)

    def update(self):
        # Прогружаем текущий режим
        self.is_active = False
        if self.saver.load_state()["sound_mode"] == "SW":
            self.is_active = True

        # Активация при наведенин курсора
        mouse_cursor = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_cursor):
            self.current_color = self.under_mouse
        else:
            if self.is_active:
                self.current_color = self.active_color
            else:
                self.current_color = self.passive_color

        # Активность при клике
        if self.rect.collidepoint(mouse_cursor):
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:
                self.saver.save_sound_mode("SW")
                self.sound_player = sound_player.SoundPlayer()
