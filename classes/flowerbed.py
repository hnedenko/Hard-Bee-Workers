from os import path
import pygame
import random


class Flowerbed(pygame.sprite.Group):
    def __init__(self, locator, all_sprites):
        pygame.sprite.Group.__init__(self)

        for i in range(5):
            position = (locator.shift_horizontal + int((8 + i * 4) * locator.block_size[0]),
                        locator.height - locator.shift_vertical - int((5 + i * 1) * locator.block_size[1]))
            self.add_flower(locator, all_sprites, position)
        for i in range(5):
            position = (locator.shift_horizontal + int((10 + i * 4) * locator.block_size[0]),
                        locator.height - locator.shift_vertical - int((3 + i * 1) * locator.block_size[1]))
            self.add_flower(locator, all_sprites, position)
        for i in range(3):
            position = (locator.shift_horizontal + int((16 + i * 4) * locator.block_size[0]),
                        locator.height - locator.shift_vertical - int((2 + i * 1) * locator.block_size[1]))
            self.add_flower(locator, all_sprites, position)
        for i in range(4):
            position = (locator.shift_horizontal + int((14 + i * 4) * locator.block_size[0]),
                        locator.height - locator.shift_vertical - int((9 + i * 1) * locator.block_size[1]))
            self.add_flower(locator, all_sprites, position)
        for i in range(3):
            position = (locator.shift_horizontal + int((16 + i * 4) * locator.block_size[0]),
                        locator.height - locator.shift_vertical - int((12 + i * 1) * locator.block_size[1]))
            self.add_flower(locator, all_sprites, position)

    def add_flower(self, locator, all_sprites, position):
        f = Flower(locator,
                   all_sprites,
                   position)
        self.add(f)


# Один цветочек
class Flower(pygame.sprite.Sprite):
    def __init__(self, locator, all_sprites, position):
        pygame.sprite.Sprite.__init__(self)

        # Расчитываем размер экземпляра цветочка
        self.size = (int(1.5 * locator.block_size[0]), int(1.5 * locator.block_size[1]))
        self.origin_position = position

        # Инициализация параметров
        self.position = [self.size[0] // 2, self.size[1] // 2]
        images_dir = path.join(path.dirname(__file__), '..')
        images_dir = path.join(images_dir, "img")
        image = pygame.image.load(path.join(images_dir, "flower.png")).convert_alpha()
        self.origin_image = pygame.transform.scale(image, self.size)
        self.image = self.origin_image
        self.rect = self.image.get_rect()
        self.rect.center = self.origin_position

        # Добавляем цветочек в группу спрайтов
        all_sprites.add(self)

        # Счётчики для случайного движения
        self.time = random.randint(0, 500)
        self.flip_time = 0
        self.period = 500 + random.randint(-50, 50)

    def update(self):
        self.time += 1

        if self.time == self.period:
            self.time = 0
            new_size = (int(self.size[0] * 0.8), int(self.size[1] * 0.8))
            self.image = pygame.transform.scale(self.origin_image, new_size)
            self.rect = self.image.get_rect()
            self.rect.center = self.origin_position
            self.flip_time = 1

        if self.flip_time != 0:
            self.flip_time += 1
        if self.flip_time == 11:
            new_size = self.size
            self.image = pygame.transform.scale(self.origin_image, new_size)
            self.rect = self.image.get_rect()
            self.rect.center = self.origin_position
            self.flip_time = 0
