from os import path
import pygame


class ImgButtonSpeedBees(pygame.sprite.Sprite):
    def __init__(self, locator, all_sprites):
        pygame.sprite.Sprite.__init__(self)

        # Расчитываем позицию и размер фона
        self.origin_size = (int(locator.block_size[0] * 3 * 0.75),
                            int(locator.block_size[1] * 1 * 0.75))
        self.origin_position = (locator.shift_horizontal + self.origin_size[0]//2 + 1.2 * locator.block_size[0],
                                locator.shift_vertical + (locator.block_size[1])//2 + 9 * locator.block_size[1])

        # Инициализация параметров фона
        self.position = [self.origin_size[0]//2, self.origin_size[1]//2]
        images_dir = path.join(path.dirname(__file__), '..')
        images_dir = path.join(images_dir, "img")
        self.origin_image = pygame.image.load(path.join(images_dir, "button.png")).convert_alpha()
        self.image = pygame.transform.scale(self.origin_image, self.origin_size)
        self.rect = self.image.get_rect()
        self.rect.center = self.origin_position

        # Добавляем фон в группу спрайтов
        all_sprites.add(self)

        # Отслеживание нажатия кнопки
        self.is_activated = False

    def update(self):
        # Активация при наведенин курсора
        mouse_cursor = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_cursor):
            self.image = pygame.transform.scale(self.origin_image,
                                                (int(self.origin_size[0] * 1.2),
                                                 int(self.origin_size[1] * 1.2)))
            self.rect.center = (self.origin_position[0] - int(self.origin_size[0] * 0.1),
                                self.origin_position[1] - int(self.origin_size[1] * 0.1))
        else:
            self.image = pygame.transform.scale(self.origin_image, self.origin_size)
            self.rect.center = self.origin_position

        # Активность при клике
        self.is_activated = False
        if self.rect.collidepoint(mouse_cursor):
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:
                self.is_activated = True
