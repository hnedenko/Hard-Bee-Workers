from os import path
import pygame


class NBees(pygame.sprite.Sprite):
    def __init__(self, locator, all_sprites):
        pygame.sprite.Sprite.__init__(self)

        # Расчитываем позицию и размер фона
        size = (locator.block_size[0] * 3,
                locator.block_size[1] * 3)
        position = (locator.shift_horizontal + size[0]//2 + int(1.5 * locator.block_size[0]),
                    locator.shift_vertical + size[1]//2 + int(1.5 * locator.block_size[1]))

        # Инициализация параметров фона
        self.position = [size[0]//2, size[1]//2]
        images_dir = path.join(path.dirname(__file__), '..')
        images_dir = path.join(images_dir, "img")
        image = pygame.image.load(path.join(images_dir, "bee_count.png")).convert_alpha()
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.rect.center = position

        # Добавляем фон в группу спрайтов
        all_sprites.add(self)

    def update(self):
        pass
