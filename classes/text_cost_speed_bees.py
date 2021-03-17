from os import path
import pygame
from classes import colors


class TextCostSpeedBees:
    def __init__(self, locator):
        size = int(0.75 * locator.block_size[0])
        position = (locator.shift_horizontal + int(locator.block_size[0] * 1.5 * 0.75) + 1.2 * locator.block_size[0],
                    locator.shift_vertical + (locator.block_size[1])//2 + 9 * locator.block_size[1])
        self.text = "749"
        self.color = colors.ORANGE
        self.size = size
        self.position = position
        font_dir = path.join(path.dirname(__file__), '..')
        font_dir = path.join(font_dir, 'res')
        self.font = path.join(font_dir, "Adigiana_2.ttf")
        self.sized_font = pygame.font.Font(self.font, self.size)
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()
        self.discharges_list = ["", "K", "M", "B", "T", "aa",
                                "ab", "ac", "ad", "ae", "af",
                                "ag", "ah", "ai", "aj", "ak",
                                "al", "am", "an", "ao", "ap",
                                "aq", "ar", "as", "at", "au",
                                "av", "aw", "ax", "ay", "az"]

    def draw(self, surface):
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()
        self.rect.center = self.position
        surface.blit(self.render, self.rect)

    def update(self, text):
        if text != "MAX":
            # Разложение на разряды
            decomposition = "0"
            i = 1000
            discharge_decomposition = dict()
            for discharge in self.discharges_list:
                discharge_decomposition[discharge] = (int(text) % i) // (i // 1000)
                i *= 1000
            # Запись в виде максимального разряда
            for discharge in reversed(self.discharges_list):
                if discharge_decomposition[discharge] != 0 and decomposition == "0":
                    decomposition = str(discharge_decomposition[discharge]) + discharge
            self.text = decomposition
        else:
            self.text = text
