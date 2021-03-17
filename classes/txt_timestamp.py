from os import path
import pygame
from classes import colors


class TxtTimeStemp:
    def __init__(self, locator):
        size = int(1 * locator.block_size[0])
        position = (locator.shift_horizontal + int(16 * locator.block_size[0]),
                    locator.shift_vertical + int(1.75 * locator.block_size[1]))
        self.text = ""
        self.color = colors.YELLOW
        self.size = size
        self.position = position
        font_dir = path.join(path.dirname(__file__), '..')
        font_dir = path.join(font_dir, 'res')
        self.font = path.join(font_dir, "Adigiana_2.ttf")
        self.sized_font = pygame.font.Font(self.font, self.size)
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()
        self.discharges_list = ["суток", "часов", "минут", "секунд"]

    def draw(self, surface):
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()
        self.rect.center = self.position
        surface.blit(self.render, self.rect)

    def update(self, text):
        if text != "0":
            # Разложение на временные интервалы
            fps_timestamp = int(text)
            days = fps_timestamp//(24*60*60*25)
            fps_timestamp -= days*24*60*60*25
            hour = fps_timestamp//(60*60*25)
            fps_timestamp -= hour*60*60*25
            minutes = fps_timestamp // (60 * 25)
            fps_timestamp -= minutes * 60 * 25
            seconds = fps_timestamp // (25)
            fps_timestamp -= seconds * 25

            # Формирование строки времени
            time_string = ""
            if days != 0:
                time_string = time_string + str(days) + " д "
            if hour != 0:
                time_string = time_string + str(hour) + " ч "
            if minutes != 0:
                time_string = time_string + str(minutes) + " мин "
            if seconds != 0:
                time_string = time_string + str(seconds) + " с"

            self.text = "Вы прошшли игру за: " + time_string
        else:
            self.text = ""
