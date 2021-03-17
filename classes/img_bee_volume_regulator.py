from os import path
import pygame
from main_classes import saver


# Класс создаёт регулятор сложности в натсройках
class BeeVolumeRegulator(pygame.sprite.Sprite):
    def __init__(self, locator, all_sprites, sound_player):
        pygame.sprite.Sprite.__init__(self)
        self.locator = locator
        self.saver = saver.Saver()
        self.sound_player = sound_player

        # Расчитываем позицию и размер
        self.origin_size = (int(self.locator.block_size[0] * 1.5),
                            int(self.locator.block_size[1] * 1.5))
        self.min = self.locator.shift_horizontal + self.origin_size[0] // 2 + 2.5 * self.locator.block_size[0]
        self.max = self.locator.shift_horizontal + self.origin_size[0] // 2 + 10 * self.locator.block_size[0]
        self.length = self.max - self.min
        self.origin_position = (self.min + int(self.saver.load_state()["volume"])*self.length/101,
                                self.locator.shift_vertical + int(9.7 * self.locator.block_size[1]))

        # Инициализация параметров фона
        self.position = [self.origin_size[0]//2, self.origin_size[1]//2]
        images_dir = path.join(path.dirname(__file__), '..')
        images_dir = path.join(images_dir, "img")
        self.origin_image = pygame.image.load(path.join(images_dir, "bee.png")).convert_alpha()
        self.image = pygame.transform.scale(self.origin_image, self.origin_size)
        self.rect = self.image.get_rect()
        self.rect.center = self.origin_position

        # Добавляем фон в группу спрайтов
        all_sprites.add(self)

    def update(self):
        mouse_cursor = pygame.mouse.get_pos()
        # Движение при клике
        if self.rect.collidepoint(mouse_cursor):
            pressed = pygame.mouse.get_pressed()
            if pressed[0] and self.min < pygame.mouse.get_pos()[0] < self.max:
                self.rect.center = (pygame.mouse.get_pos()[0], self.rect.center[1])
                volume = int(((mouse_cursor[0] - self.min)/self.length)*101)
                self.saver.save_volume(volume)
                self.sound_player.set_volume(volume)

    def draw(self):
        pass
