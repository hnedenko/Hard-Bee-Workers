import pygame
from classes import colors
from classes import background
from classes import framer
from classes import hive
from classes import button_new_game
from classes import button_load_game
from classes import button_settings
from classes import button_exit_game


class MenuObjects:
    def __init__(self, screen, locator, level_upper):
        self.screen = screen
        self.locator = locator
        self.go_to = ""
        self.exit = False

        # Объекты меню
        self.sprites = pygame.sprite.Group()

        # Пергаментный фон
        self.background = background.BackGround(self.locator, self.sprites)
        # Рамка
        self.frame = framer.MenuFrame(self.locator, self.sprites)
        # Улики
        self.left_hive = hive.LeftHive(self.locator, self.sprites)
        self.right_hive = hive.RightHive(self.locator, self.sprites)
        # Надписи-кнопки
        self.btn_new_game = button_new_game.ButtonNewGame(self.locator)
        self.btn_load_game = button_load_game.ButtonLoadGame(self.locator)
        self.btn_settings = button_settings.ButtonSettings(self.locator)
        self.btn_exit_game = button_exit_game.ButtonExitGame(self.locator)

    def save_state(self):
        pass

    def load_state(self):
        pass

    def update(self):
        # Маркировка перехода в новый режим, если надо или обновление объектов
        if self.btn_new_game.is_activated:
            self.go_to = "GAME_NEW"
        elif self.btn_load_game.is_activated:
            self.go_to = "GAME_LOAD"
        elif self.btn_settings.is_activated:
            self.go_to = "SETTINGS"
        elif self.btn_exit_game.is_activated:
            self.exit = True
        else:
            self.sprites.update()
            self.btn_new_game.update()
            self.btn_load_game.update()
            self.btn_settings.update()
            self.btn_exit_game.update()

    def draw(self):
        # Отрисовка объектов
        self.screen.fill(colors.BLACK)
        self.sprites.draw(self.screen)
        self.btn_new_game.draw(self.screen)
        self.btn_load_game.draw(self.screen)
        self.btn_settings.draw(self.screen)
        self.btn_exit_game.draw(self.screen)
