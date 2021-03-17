from os import path
import pygame
from classes import colors


class TextAbout00:
    def __init__(self, locator):
        size = int(1 * locator.block_size[0])
        position = (locator.width - locator.shift_horizontal - int(7 * locator.block_size[0]),
                    locator.shift_vertical + int(2 * locator.block_size[1]))
        self.text = "Развей свой улик"
        self.color = colors.GREEN
        self.size = size
        self.position = position
        font_dir = path.join(path.dirname(__file__), '..')
        font_dir = path.join(font_dir, 'res')
        self.font = path.join(font_dir, "Adigiana_2.ttf")
        self.sized_font = pygame.font.Font(self.font, self.size)
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()

    def draw(self, surface):
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()
        self.rect.center = self.position
        surface.blit(self.render, self.rect)

    def update(self):
        pass


class TextAbout01:
    def __init__(self, locator):
        size = int(1 * locator.block_size[0])
        position = (locator.width - locator.shift_horizontal - int(7 * locator.block_size[0]),
                    locator.shift_vertical + int(3 * locator.block_size[1]))
        self.text = "до МАКСИМУМА!"
        self.color = colors.GREEN
        self.size = size
        self.position = position
        font_dir = path.join(path.dirname(__file__), '..')
        font_dir = path.join(font_dir, 'res')
        self.font = path.join(font_dir, "Adigiana_2.ttf")
        self.sized_font = pygame.font.Font(self.font, self.size)
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()

    def draw(self, surface):
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()
        self.rect.center = self.position
        surface.blit(self.render, self.rect)

    def update(self):
        pass


class TextAbout02:
    def __init__(self, locator):
        size = int(1 * locator.block_size[0])
        position = (locator.width - locator.shift_horizontal - int(7 * locator.block_size[0]),
                    locator.shift_vertical + int(5 * locator.block_size[1]))
        self.text = "Увеличивай:"
        self.color = colors.GREEN
        self.size = size
        self.position = position
        font_dir = path.join(path.dirname(__file__), '..')
        font_dir = path.join(font_dir, 'res')
        self.font = path.join(font_dir, "Adigiana_2.ttf")
        self.sized_font = pygame.font.Font(self.font, self.size)
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()

    def draw(self, surface):
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()
        self.rect.center = self.position
        surface.blit(self.render, self.rect)

    def update(self):
        pass


class TextAbout03:
    def __init__(self, locator):
        size = int(1 * locator.block_size[0])
        position = (locator.width - locator.shift_horizontal - int(7 * locator.block_size[0]),
                    locator.shift_vertical + int(6 * locator.block_size[1]))
        self.text = "- количество пчёлок -"
        self.color = colors.GREEN
        self.size = size
        self.position = position
        font_dir = path.join(path.dirname(__file__), '..')
        font_dir = path.join(font_dir, 'res')
        self.font = path.join(font_dir, "Adigiana_2.ttf")
        self.sized_font = pygame.font.Font(self.font, self.size)
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()

    def draw(self, surface):
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()
        self.rect.center = self.position
        surface.blit(self.render, self.rect)

    def update(self):
        pass


class TextAbout04:
    def __init__(self, locator):
        size = int(1 * locator.block_size[0])
        position = (locator.width - locator.shift_horizontal - int(7 * locator.block_size[0]),
                    locator.shift_vertical + int(7 * locator.block_size[1]))
        self.text = "- скорость полёта -"
        self.color = colors.GREEN
        self.size = size
        self.position = position
        font_dir = path.join(path.dirname(__file__), '..')
        font_dir = path.join(font_dir, 'res')
        self.font = path.join(font_dir, "Adigiana_2.ttf")
        self.sized_font = pygame.font.Font(self.font, self.size)
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()

    def draw(self, surface):
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()
        self.rect.center = self.position
        surface.blit(self.render, self.rect)

    def update(self):
        pass


class TextAbout05:
    def __init__(self, locator):
        size = int(1 * locator.block_size[0])
        position = (locator.width - locator.shift_horizontal - int(7 * locator.block_size[0]),
                    locator.shift_vertical + int(8 * locator.block_size[1]))
        self.text = "- количество нектара,"
        self.color = colors.GREEN
        self.size = size
        self.position = position
        font_dir = path.join(path.dirname(__file__), '..')
        font_dir = path.join(font_dir, 'res')
        self.font = path.join(font_dir, "Adigiana_2.ttf")
        self.sized_font = pygame.font.Font(self.font, self.size)
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()

    def draw(self, surface):
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()
        self.rect.center = self.position
        surface.blit(self.render, self.rect)

    def update(self):
        pass


class TextAbout06:
    def __init__(self, locator):
        size = int(1 * locator.block_size[0])
        position = (locator.width - locator.shift_horizontal - int(7 * locator.block_size[0]),
                    locator.shift_vertical + int(9 * locator.block_size[1]))
        self.text = "приносимого за раз -"
        self.color = colors.GREEN
        self.size = size
        self.position = position
        font_dir = path.join(path.dirname(__file__), '..')
        font_dir = path.join(font_dir, 'res')
        self.font = path.join(font_dir, "Adigiana_2.ttf")
        self.sized_font = pygame.font.Font(self.font, self.size)
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()

    def draw(self, surface):
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()
        self.rect.center = self.position
        surface.blit(self.render, self.rect)

    def update(self):
        pass


class TextAbout07:
    def __init__(self, locator):
        size = int(1 * locator.block_size[0])
        position = (locator.width - locator.shift_horizontal - int(7 * locator.block_size[0]),
                    locator.shift_vertical + int(11 * locator.block_size[1]))
        self.text = "Стань самым умелым"
        self.color = colors.GREEN
        self.size = size
        self.position = position
        font_dir = path.join(path.dirname(__file__), '..')
        font_dir = path.join(font_dir, 'res')
        self.font = path.join(font_dir, "Adigiana_2.ttf")
        self.sized_font = pygame.font.Font(self.font, self.size)
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()

    def draw(self, surface):
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()
        self.rect.center = self.position
        surface.blit(self.render, self.rect)

    def update(self):
        pass


class TextAbout08:
    def __init__(self, locator):
        size = int(1 * locator.block_size[0])
        position = (locator.width - locator.shift_horizontal - int(7 * locator.block_size[0]),
                    locator.shift_vertical + int(12 * locator.block_size[1]))
        self.text = "!ПАСЕЧНИКОМ!"
        self.color = colors.GREEN
        self.size = size
        self.position = position
        font_dir = path.join(path.dirname(__file__), '..')
        font_dir = path.join(font_dir, 'res')
        self.font = path.join(font_dir, "Adigiana_2.ttf")
        self.sized_font = pygame.font.Font(self.font, self.size)
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()

    def draw(self, surface):
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()
        self.rect.center = self.position
        surface.blit(self.render, self.rect)

    def update(self):
        pass


class TextAbout09:
    def __init__(self, locator):
        size = int(1 * locator.block_size[0])
        position = (locator.width - locator.shift_horizontal - int(9 * locator.block_size[0]),
                    locator.shift_vertical + int(14 * locator.block_size[1]))
        self.text = "(c) Alex Hnedenko"
        self.color = colors.GREEN
        self.size = size
        self.position = position
        font_dir = path.join(path.dirname(__file__), '..')
        font_dir = path.join(font_dir, 'res')
        self.font = path.join(font_dir, "Adigiana_2.ttf")
        self.sized_font = pygame.font.Font(self.font, self.size)
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()

    def draw(self, surface):
        self.render = self.sized_font.render(self.text, True, self.color)
        self.rect = self.render.get_rect()
        self.rect.center = self.position
        surface.blit(self.render, self.rect)

    def update(self):
        pass
