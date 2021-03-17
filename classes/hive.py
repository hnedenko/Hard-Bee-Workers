from os import path
import pygame


# Класс создаёт левый улей
class LeftHive(pygame.sprite.Sprite):
    def __init__(self, locator, all_sprites):
        pygame.sprite.Sprite.__init__(self)

        # Расчитываем позицию и размер фона
        size = (locator.block_size[0] * 5,
                locator.block_size[1] * 5)
        position = (locator.shift_horizontal + size[0]//2 + locator.block_size[0],
                    locator.height - locator.shift_vertical - size[1]//2 - locator.block_size[1])

        # Инициализация параметров фона
        self.position = [size[0]//2, size[1]//2]
        images_dir = path.join(path.dirname(__file__), '..')
        images_dir = path.join(images_dir, "img")
        image = pygame.image.load(path.join(images_dir, "hive.png")).convert_alpha()
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.rect.center = position

        # Добавляем фон в группу спрайтов
        all_sprites.add(self)

    def update(self):
        pass


# Класс создаёт левый улей
class RightHive(pygame.sprite.Sprite):
    def __init__(self, locator, all_sprites):
        pygame.sprite.Sprite.__init__(self)

        # Расчитываем позицию и размер фона
        size = (locator.block_size[0] * 5,
                locator.block_size[1] * 5)
        position = (locator.width - locator.shift_horizontal - size[0]//2 - locator.block_size[0],
                    locator.height - locator.shift_vertical - size[1]//2 - locator.block_size[1])

        # Инициализация параметров фона
        self.position = [size[0]//2, size[1]//2]
        images_dir = path.join(path.dirname(__file__), '..')
        images_dir = path.join(images_dir, "img")
        image = pygame.image.load(path.join(images_dir, "hive.png")).convert_alpha()
        image = pygame.transform.flip(image, True, False)
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.rect.center = position

        # Добавляем фон в группу спрайтов
        all_sprites.add(self)

    def update(self):
        pass


# Класс создаёт улей в игре
class Hive(pygame.sprite.Sprite):
    def __init__(self, locator, all_sprites):
        pygame.sprite.Sprite.__init__(self)

        # Расчитываем позицию и размер фона
        size = (locator.block_size[0] * 5,
                locator.block_size[1] * 5)
        position = (locator.shift_horizontal + size[0]//2 + 6 * locator.block_size[0],
                    locator.shift_vertical + size[1]//2 + 2 * locator.block_size[1])

        # Инициализация параметров фона
        self.position = [size[0]//2, size[1]//2]
        images_dir = path.join(path.dirname(__file__), '..')
        images_dir = path.join(images_dir, "img")
        image = pygame.image.load(path.join(images_dir, "hive.png")).convert_alpha()
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.rect.center = position

        # Добавляем фон в группу спрайтов
        all_sprites.add(self)

    def update(self):
        pass
