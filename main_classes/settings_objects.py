import pygame
from classes import colors
from classes import background
from classes import framer
from classes import button_quit
from classes import text_difficulty
from classes import text_volume
from classes import text_volume_regulator
from classes import text_difficulty_regulator
from classes import img_bee_difficulty_regulator
from classes import img_bee_volume_regulator
from classes import text_bee_difficulty_regulator
from classes import text_bee_volume_regulator
from classes import text_about
from classes import text_winni
from classes import text_SW
from main_classes import saver


class SettingsObjects:
    def __init__(self, screen, locator, level_upper, sound_player):
        self.screen = screen
        self.locator = locator
        self.sound_player = sound_player
        self.saver = saver.Saver()
        self.go_to = ""
        self.exit = False

        # Объекты настроек
        self.sprites = pygame.sprite.Group()
        self.bee_regulators = pygame.sprite.Group()

        # Пергаментный фон
        self.background = background.BackGround(self.locator, self.sprites)
        # Рамка
        self.frame = framer.SettingsFrame(self.locator, self.sprites)
        # Надписи-кнопки
        self.btn_quit = button_quit.ButtonQuit(self.locator)
        # Обычные надписи
        self.text_difficulty = text_difficulty.TextDifficulty(self.locator)
        self.text_volume = text_volume.TextVolume(self.locator)
        # Объекты регулятора громкости
        self.text_volume_regulator = text_volume_regulator.TextVolumeRegulator(self.locator)
        self.img_bee_volume_regulator = img_bee_volume_regulator.BeeVolumeRegulator(self.locator,
                                                                                    self.sprites,
                                                                                    self.sound_player)
        self.bee_regulators.add(self.img_bee_volume_regulator)
        self.text_bee_volume_regulator = text_bee_volume_regulator.TextBeeVolumeRegulator(self.locator,
                                                                                          self.saver.load_state()["volume"])
        # Объекты регулятора сложности
        self.text_difficulty_regulator = text_difficulty_regulator.TextDifficultyRegulator(self.locator)
        self.img_bee_difficulty_regulator = img_bee_difficulty_regulator.BeeDifficultyRegulator(self.locator,
                                                                                                self.sprites)
        self.bee_regulators.add(self.img_bee_difficulty_regulator)
        self.text_bee_difficulty_regulator = text_bee_difficulty_regulator.TextBeeDifficultyRegulator(self.locator,
                                                                                                      self.saver.load_state()["difficulty"])
        # Текст "О разработчиках"
        self.text_about_00 = text_about.TextAbout00(self.locator)
        self.text_about_01 = text_about.TextAbout01(self.locator)
        self.text_about_02 = text_about.TextAbout02(self.locator)
        self.text_about_03 = text_about.TextAbout03(self.locator)
        self.text_about_04 = text_about.TextAbout04(self.locator)
        self.text_about_05 = text_about.TextAbout05(self.locator)
        self.text_about_06 = text_about.TextAbout06(self.locator)
        self.text_about_07 = text_about.TextAbout07(self.locator)
        self.text_about_08 = text_about.TextAbout08(self.locator)
        self.text_about_09 = text_about.TextAbout09(self.locator)

        # Переключение режимов звука
        self.text_winni = text_winni.TextWinni(self.locator, self.saver, self.sound_player)
        self.text_SW = text_SW.TextSW(self.locator, self.saver, self.sound_player)

    def save_state(self):
        pass

    def load_state(self):
        pass

    def update(self):
        # Маркировка перехода в новый режим, если надо или обновление объектов
        if self.btn_quit.is_activated:
            self.go_to = "MENU"
        else:
            self.sprites.update()
            self.btn_quit.update()
            self.text_difficulty.update()
            self.text_volume.update()
            self.text_volume_regulator.update()
            self.text_difficulty_regulator.update()
            self.text_bee_difficulty_regulator.update(self.saver.load_state()["difficulty"],
                                                      self.img_bee_difficulty_regulator.rect.centerx)
            self.text_bee_volume_regulator.update(self.saver.load_state()["volume"],
                                                  self.img_bee_volume_regulator.rect.centerx)
            self.text_about_00.update()
            self.text_about_01.update()
            self.text_about_02.update()
            self.text_about_03.update()
            self.text_about_04.update()
            self.text_about_05.update()
            self.text_about_06.update()
            self.text_about_07.update()
            self.text_about_08.update()
            self.text_about_09.update()
            self.text_winni.update()
            self.text_SW.update()

    def draw(self):
        # Отрисовка объектов
        self.screen.fill(colors.BLACK)
        self.sprites.draw(self.screen)
        self.btn_quit.draw(self.screen)
        self.text_difficulty.draw(self.screen)
        self.text_volume.draw(self.screen)
        self.text_volume_regulator.draw(self.screen)
        self.text_difficulty_regulator.draw(self.screen)
        self.bee_regulators.draw(self.screen)
        self.text_bee_difficulty_regulator.draw(self.screen)
        self.text_bee_volume_regulator.draw(self.screen)
        self.text_about_00.draw(self.screen)
        self.text_about_01.draw(self.screen)
        self.text_about_02.draw(self.screen)
        self.text_about_03.draw(self.screen)
        self.text_about_04.draw(self.screen)
        self.text_about_05.draw(self.screen)
        self.text_about_06.draw(self.screen)
        self.text_about_07.draw(self.screen)
        self.text_about_08.draw(self.screen)
        self.text_about_09.draw(self.screen)
        self.text_winni.draw(self.screen)
        self.text_SW.draw(self.screen)
