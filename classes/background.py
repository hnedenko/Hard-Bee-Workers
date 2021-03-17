from os import path
import pygame


# Класс создаёт фон пергаментного цвета
class BackGround(pygame.sprite.Sprite):
    def __init__(self, locator, all_sprites):
        pygame.sprite.Sprite.__init__(self)

        # Расчитываем позицию и размер фона
        position = (locator.width // 2,
                    locator.height // 2)
        size = (locator.width - locator.shift_horizontal * 2,
                locator.height - locator.shift_vertical * 2)

        # Инициализация параметров фона
        self.position = [size[0]//2, size[1]//2]
        images_dir = path.join(path.dirname(__file__), '..')
        images_dir = path.join(images_dir, "img")
        image = pygame.image.load(path.join(images_dir, "bg.png")).convert_alpha()
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.rect.center = position

        # Добавляем фон в группу спрайтов
        all_sprites.add(self)

    def update(self):
        pass
