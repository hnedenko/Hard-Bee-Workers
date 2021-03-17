import pygame
from win32api import GetSystemMetrics
import game_objects
from classes import colors
from main_classes import sound_player


class GameManager():
    def __init__(self):
        # Глобальные константы
        self.FPS = 25

        # Подстройка под экран пользователя
        self.WIDTH = GetSystemMetrics(0)
        self.HEIGHT = GetSystemMetrics(1)

        # Инициализация Pygame игры
        pygame.init()
        self.sound_player = sound_player.SoundPlayer()
        pygame.mouse.set_visible(False)
        flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN | pygame.SCALED
        pygame.display.set_caption("Hard Workers Bees")
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT), flags)
        self.CLOCK = pygame.time.Clock()

        # Создание менеджера объектов игры
        self.game_objects = game_objects.GameObject(self.SCREEN, self.WIDTH, self.HEIGHT, self.sound_player)

    def play(self):
        # Цикл игры
        running = True
        while running:
            # Держим цикл на правильной скорости
            self.CLOCK.tick(self.FPS)

            # Отслеживание действий игрока
            for event in pygame.event.get():
                # Перехват закрытия окна
                if event.type == pygame.QUIT:
                    running = False
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    running = False
                if self.game_objects.exit:
                    running = False

            # Обновляем объекты
            self.game_objects.update()

            # Отрисовываем объекты
            self.game_objects.draw()
            # Курсор
            pygame.draw.circle(self.SCREEN, colors.GREEN,
                               (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 20)
            pygame.draw.circle(self.SCREEN, colors.YELLOW,
                               (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 10)
            pygame.draw.circle(self.SCREEN, colors.BLACK,
                               (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 2)
            pygame.display.flip()
        pygame.quit()
