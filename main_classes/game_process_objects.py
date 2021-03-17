import pygame
from classes import colors
from classes import background
from classes import framer
from classes import button_quit
from classes import hive
from classes import queen_bee
from classes import flowerbed
from classes import text_money
from classes import n_bees
from classes import speed_bees
from classes import profit_bees
from classes import text_numbers_bees
from classes import text_speed_bees
from classes import text_profit_bees
from classes import img_button_n_bees
from classes import img_button_speed_bees
from classes import img_button_profit_bees
from classes import text_level_n_bees
from classes import text_level_speed_bees
from classes import text_level_profit_bees
from classes import text_cost_n_bees
from classes import text_cost_speed_bees
from classes import text_cost_profit_bees
from classes import txt_timestamp
from classes import txt_time
from main_classes import saver
from main_classes import sound_player


class GameProcessObjects:
    def __init__(self, screen, locator, level_upper, sound_player, mode):
        self.screen = screen
        self.locator = locator
        self.sound_player = sound_player
        self.level_upper = level_upper
        self.saver = saver.Saver()
        self.go_to = ""
        self.exit = False

        # Объекты игры
        self.sprites = pygame.sprite.Group()

        # Начальное состояние игры, если режим "NEW"
        if mode == "NEW":
            self.money = 1
            self.i_level_n_bees = 0
            self.level_n_bees = level_upper.number[self.i_level_n_bees]
            self.i_level_speed_bees = 0
            self.level_speed_bees = level_upper.speed[self.i_level_speed_bees]
            self.i_level_money_profit = 0
            self.level_money_profit = level_upper.profit[self.i_level_money_profit]
            self.time = 0
            self.timestamp = 0
            self.saver.save_state(self.money, self.i_level_n_bees, self.i_level_speed_bees,
                                  self.i_level_money_profit, self.time, self.timestamp)

        # Загрузка сохранённого состояния, если режим "LOAD"
        if mode == "LOAD":
            self.load_state()

        # Пергаментный фон
        self.background = background.BackGround(self.locator, self.sprites)
        # Рамка
        self.frame = framer.GameFrame(self.locator, self.sprites)
        # Надписи-кнопки
        self.btn_quit = button_quit.ButtonQuit(self.locator)
        # Улик
        self.hive = hive.Hive(self.locator, self.sprites)
        # Цветочки
        self.flowerbed = flowerbed.Flowerbed(self.locator, self.sprites)
        # Пчелки
        self.bees_flock = queen_bee.BeesFlock(self.locator, self.sprites, self.flowerbed, self.level_speed_bees)
        for i in range(self.level_n_bees):
            self.bees_flock.add_bee()
        # Показ собраных денег
        self.text_money = text_money.TextMoney(self.locator, str(int(self.money)))
        # Скиллы
        self.n_bees = n_bees.NBees(self.locator, self.sprites)
        self.speed_bees = speed_bees.SpeedBees(self.locator, self.sprites)
        self.profit_bees = profit_bees.ProfitBees(self.locator, self.sprites)
        # Надписи типов скилов
        self.text_numbers_bees = text_numbers_bees.NumbersBees(locator)
        self.text_speed_bees = text_speed_bees.SpeedBees(locator)
        self.text_profit_bees = text_profit_bees.ProfitBees(locator)
        # Картинки кнопок
        self.img_button_n_bees = img_button_n_bees.ImgButtonNBees(self.locator, self.sprites)
        self.img_button_speed_bees = img_button_speed_bees.ImgButtonSpeedBees(self.locator, self.sprites)
        self.img_button_profit_bees = img_button_profit_bees.ImgButtonProfitBees(self.locator, self.sprites)
        # Показ текущего уровня апгрейдов
        self.text_level_n_bees = text_level_n_bees.TextLevelNBees(self.locator, str(int(self.level_n_bees)))
        self.text_level_speed_bees = text_level_speed_bees.TextLevelSpeedBees(self.locator,
                                                                              str(int(self.level_speed_bees)))
        self.text_level_profit_bees = text_level_profit_bees.TextLevelProfitBees(self.locator,
                                                                                 str(int(self.level_money_profit)))
        # Показ текущей следующей стоимости апгрейдов
        self.text_cost_n_bees = text_cost_n_bees.TextCostNBees(locator)
        self.text_cost_speed_bees = text_cost_speed_bees.TextCostSpeedBees(locator)
        self.text_cost_profit_bees = text_cost_profit_bees.TextCostProfitBees(locator)

        # Показ таймстемпа
        self.txt_timestamp = txt_timestamp.TxtTimeStemp(locator)
        self.txt_time = txt_time.TxtTime(locator)

    def save_state(self):
        self.saver.save_state(self.money,
                              self.i_level_n_bees,
                              self.i_level_speed_bees,
                              self.i_level_money_profit,
                              self.time,
                              self.timestamp)

    def load_state(self):
        readed_dict = self.saver.load_state()
        self.money = int(readed_dict["money"])
        self.i_level_n_bees = int(readed_dict["level_n_bees"])
        self.i_level_speed_bees = int(readed_dict["level_speed_bees"])
        self.i_level_money_profit = int(readed_dict["level_money_profit"])
        self.timestamp = int(readed_dict["timestamp"])
        self.level_n_bees = self.level_upper.number[self.i_level_n_bees]
        self.level_speed_bees = self.level_upper.speed[self.i_level_speed_bees]
        self.level_money_profit = self.level_upper.profit[self.i_level_money_profit]
        self.time = int(readed_dict["time"])
        self.timestamp = int(readed_dict["timestamp"])

    def update(self):
        # Маркировка перехода в новый режим, если надо или обновление объектов
        if self.btn_quit.is_activated:
            self.go_to = "MENU"
        else:
            self.sprites.update()
            self.btn_quit.update()
            self.text_money.update(str(int(self.money)))
            self.text_numbers_bees.update()
            self.text_speed_bees.update()
            self.text_profit_bees.update()
            self.text_level_n_bees.update(str(int(self.level_n_bees)))
            self.text_level_speed_bees.update(str(int(self.level_speed_bees)))
            self.text_level_profit_bees.update(str(int(self.level_money_profit)))
            if self.i_level_n_bees + 1 < len(self.level_upper.number):
                self.text_cost_n_bees.update(
                    str(int(self.level_upper.number_cost[self.i_level_n_bees])))
            else:
                self.text_cost_n_bees.update("MAX")
            if self.i_level_speed_bees + 1 < len(self.level_upper.speed):
                self.text_cost_speed_bees.update(
                    str(int(self.level_upper.speed_cost[self.i_level_speed_bees])))
            else:
                self.text_cost_speed_bees.update("MAX")
            if self.i_level_money_profit + 1 < len(self.level_upper.profit):
                self.text_cost_profit_bees.update(
                    str(int(self.level_upper.profit_cost[self.i_level_money_profit])))
            else:
                self.text_cost_profit_bees.update("MAX")

        # Создание ещё одной плёлки
        if self.img_button_n_bees.is_activated:
            self.img_button_n_bees.is_activated = False
            if self.i_level_n_bees+1 < len(self.level_upper.number):
                if self.money >= int(self.level_upper.number_cost[self.i_level_n_bees]):
                    self.money -= int(self.level_upper.number_cost[self.i_level_n_bees])
                    self.i_level_n_bees += 1

                    if (self.i_level_n_bees == 24) and \
                            (self.i_level_speed_bees == 24) and \
                            (self.i_level_money_profit == 24):
                        self.timestamp = self.time

                    # Сохранение параметров игры
                    self.saver.save_state(self.money, self.i_level_n_bees, self.i_level_speed_bees,
                                          self.i_level_money_profit, self.time, self.timestamp)
                    self.level_n_bees = self.level_upper.number[self.i_level_n_bees]
                    for i in range(self.level_n_bees - self.level_upper.number[self.i_level_n_bees - 1]):
                        self.bees_flock.add_bee()

        # Увеличение скорости пчёлок
        if self.img_button_speed_bees.is_activated:
            self.img_button_speed_bees.is_activated = False
            if self.i_level_speed_bees+1 < len(self.level_upper.speed):
                if self.money >= self.level_upper.speed_cost[self.i_level_speed_bees]:
                    self.money -= self.level_upper.speed_cost[self.i_level_speed_bees]
                    self.i_level_speed_bees += 1

                    if (self.i_level_n_bees == 24) and \
                            (self.i_level_speed_bees == 24) and \
                            (self.i_level_money_profit == 24):
                        self.timestamp = self.time

                    # Сохранение параметров игры
                    self.saver.save_state(self.money, self.i_level_n_bees, self.i_level_speed_bees,
                                          self.i_level_money_profit, self.time, self.timestamp)
                    self.level_speed_bees = self.level_upper.speed[self.i_level_speed_bees]
                    self.bees_flock.speed = self.level_speed_bees
                    for bee in self.bees_flock:
                        bee.speed = self.level_speed_bees

        # Увеличение дохода от пчёлок
        if self.img_button_profit_bees.is_activated:
            self.img_button_profit_bees.is_activated = False
            if self.i_level_money_profit+1 < len(self.level_upper.profit):
                if self.money >= self.level_upper.profit_cost[self.i_level_money_profit]:
                    self.money -= self.level_upper.profit_cost[self.i_level_money_profit]
                    self.i_level_money_profit += 1

                    if (self.i_level_n_bees == 24) and\
                            (self.i_level_speed_bees == 24) and\
                            (self.i_level_money_profit == 24):
                        self.timestamp = self.time

                    # Сохранение параметров игры
                    self.saver.save_state(self.money, self.i_level_n_bees, self.i_level_speed_bees,
                                          self.i_level_money_profit, self.time, self.timestamp)
                    self.level_money_profit = self.level_upper.profit[self.i_level_money_profit]

        # Добавление дохода от пчёлок
        for bee in self.bees_flock:
            if bee.profit:
                self.money += self.level_money_profit
                bee.profit = False
        # Сохранение параметров игры
        self.saver.save_state(self.money, self.i_level_n_bees, self.i_level_speed_bees,
                              self.i_level_money_profit, self.time, self.timestamp)

        # Счетчик времени игры
        self.time += 1

        # Показ таймстемпа
        self.txt_timestamp.update(str(self.timestamp))
        self.txt_time.update(str(self.time))

    def draw(self):
        # Отрисовка объектов
        self.screen.fill(colors.BLACK)
        self.sprites.draw(self.screen)
        self.btn_quit.draw(self.screen)
        self.text_money.draw(self.screen)
        self.text_numbers_bees.draw(self.screen)
        self.text_speed_bees.draw(self.screen)
        self.text_profit_bees.draw(self.screen)
        self.text_level_n_bees.draw(self.screen)
        self.text_level_speed_bees.draw(self.screen)
        self.text_level_profit_bees.draw(self.screen)
        self.text_cost_n_bees.draw(self.screen)
        self.text_cost_speed_bees.draw(self.screen)
        self.text_cost_profit_bees.draw(self.screen)
        self.txt_timestamp.draw(self.screen)
        self.txt_time.draw(self.screen)
