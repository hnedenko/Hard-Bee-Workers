from os import path
import pygame
import random
import math


class BeesFlock(pygame.sprite.Group):
    def __init__(self, locator, all_sprites, flowerbed, speed):
        pygame.sprite.Group.__init__(self)

        self.locator = locator
        self.all_sprites = all_sprites
        self.flowerbed = flowerbed
        self.speed = speed

    def add_bee(self):
        f = Bee(self.locator,
                self.all_sprites,
                self.flowerbed,
                self.speed)
        self.add(f)


# Одна пчёлка
class Bee(pygame.sprite.Sprite):
    def __init__(self, locator, all_sprites, flowerbed, speed, position=""):
        pygame.sprite.Sprite.__init__(self)

        # Расчитываем размер экземпляра пчелки
        self.size = locator.block_size

        # Инициализация параметров
        self.position = [self.size[0] // 2, self.size[1] // 2]
        images_dir = path.join(path.dirname(__file__), '..')
        images_dir = path.join(images_dir, "img")
        images_dir = path.join(images_dir, "bee")
        self.origin_images = list()
        self.origin_images.append(pygame.image.load(path.join(images_dir, "bee_01.png")).convert_alpha())
        self.origin_images.append(pygame.image.load(path.join(images_dir, "bee_02.png")).convert_alpha())
        self.origin_images.append(pygame.image.load(path.join(images_dir, "bee_03.png")).convert_alpha())
        self.origin_images.append(pygame.image.load(path.join(images_dir, "bee_04.png")).convert_alpha())
        self.image = pygame.transform.scale(self.origin_images[0], self.size)
        self.rect = self.image.get_rect()

        # Позиция пчёлки
        hive_size = (locator.block_size[0] * 5,
                     locator.block_size[1] * 5)
        hive_position = (locator.shift_horizontal + hive_size[0] // 2 + 6 * locator.block_size[0],
                         locator.shift_vertical + hive_size[1] // 2 + 2 * locator.block_size[1])
        if position == "":
            position = (random.randint(hive_position[0] - hive_size[0]//5, hive_position[0] + hive_size[0]//5),
                        random.randint(hive_position[1] - hive_size[1]//5, hive_position[1] + hive_size[1]//5))
        self.home_position = position
        self.rect.center = position

        # Добавляем пчёлку в группу спрайтов
        all_sprites.add(self)

        # Номер frame
        self.frame = 0

        # Состояние пчелки
        self.state = "FLOWER"
        self.state = "HIVE"

        # Список центров цветочков и целевых точек
        self.speed = speed
        self.profit = False
        self.goal_point = self.home_position
        self.nectar = 0
        self.flower_centers = list()
        for sprite in flowerbed:
            if sprite.rect.center not in self.flower_centers:
                self.flower_centers.append(sprite.rect.center)

    @staticmethod
    def get_distance(point_01, point_02):
        return math.hypot(point_01[0] - point_02[0], point_01[1] - point_02[1])

    def update(self):
        # Пересчет frame
        if self.frame != 3:
            self.frame += 1
        else:
            self.frame = 0

        # Анимация, переход на новый frame
        self.image = pygame.transform.scale(self.origin_images[self.frame], self.size)

        # Движение к цели
        if self.get_distance(self.rect.center, self.goal_point) > self.speed:
            angle = math.atan2((self.goal_point[1] - self.rect.centery),
                               (self.goal_point[0] - self.rect.centerx))
            self.rect.centerx += self.speed * math.cos(angle)
            self.rect.centery += self.speed * math.sin(angle)
        elif self.rect.center[0] != self.goal_point[0] or self.rect.center[1] != self.goal_point[1]:
            self.rect.center = self.goal_point
        else:
            pass

        # Разворот, если летит справо
        if self.rect.center[0] < self.goal_point[0]:
            self.image = pygame.transform.flip(self.image, True, False)

        # Если "HIVE", лететь к цветку
        if self.state == "HIVE" and self.goal_point == self.rect.center:
            if self.nectar == 0:
                self.state = "FLOWER"
                self.goal_point = random.choice(self.flower_centers)
            elif self.nectar == 5:
                self.profit = True
                self.nectar -= 1
            else:
                self.nectar -= 1

        # Если "FLOWER", лететь домой
        if self.state == "FLOWER" and self.goal_point == self.rect.center:
            self.state = "HIVE"
            self.profit = 0
            self.goal_point = self.home_position
            self.nectar = 5
