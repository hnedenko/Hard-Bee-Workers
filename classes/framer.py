from os import path
import pygame


class MenuFrame(pygame.sprite.Group):
    def __init__(self, locator, all_sprites):
        pygame.sprite.Group.__init__(self)

        # Левая часть рамки
        for i in range(locator.n_vertical):
            f = Frame(locator,
                      (locator.shift_horizontal + locator.block_size[0] // 2,
                       locator.shift_vertical + locator.block_size[1] // 2 + i*locator.block_size[1]),
                      all_sprites)
            self.add(f)

        # Правая часть рамки
        for i in range(locator.n_vertical):
            f = Frame(locator,
                      (locator.width - locator.shift_horizontal - locator.block_size[0] // 2,
                       locator.shift_vertical + locator.block_size[1] // 2 + i * locator.block_size[1]),
                      all_sprites)
            self.add(f)

        # Верхняя часть рамки
        for i in range(locator.n_horizontal - 2):
            f = Frame(locator,
                      (locator.shift_horizontal + locator.block_size[0] // 2 + (i + 1) * locator.block_size[0],
                       locator.shift_vertical + locator.block_size[1] // 2),
                      all_sprites)
            self.add(f)

        # Нижняя часть рамки
        for i in range(locator.n_horizontal - 2):
            f = Frame(locator,
                      (locator.shift_horizontal + locator.block_size[0] // 2 + (i + 1) * locator.block_size[0],
                       locator.height - locator.shift_vertical - locator.block_size[1] // 2),
                      all_sprites)
            self.add(f)


class SettingsFrame(pygame.sprite.Group):
    def __init__(self, locator, all_sprites):
        pygame.sprite.Group.__init__(self)

        # Левая часть рамки
        for i in range(locator.n_vertical):
            f = Frame(locator,
                      (locator.shift_horizontal + locator.block_size[0] // 2,
                       locator.shift_vertical + locator.block_size[1] // 2 + i*locator.block_size[1]),
                      all_sprites)
            self.add(f)

        # Правая часть рамки
        for i in range(locator.n_vertical):
            f = Frame(locator,
                      (locator.width - locator.shift_horizontal - locator.block_size[0] // 2,
                       locator.shift_vertical + locator.block_size[1] // 2 + i * locator.block_size[1]),
                      all_sprites)
            self.add(f)

        # Верхняя часть рамки
        for i in range(locator.n_horizontal - 2):
            f = Frame(locator,
                      (locator.shift_horizontal + locator.block_size[0] // 2 + (i + 1) * locator.block_size[0],
                       locator.shift_vertical + locator.block_size[1] // 2),
                      all_sprites)
            self.add(f)

        # Нижняя часть рамки
        for i in range(locator.n_horizontal - 2):
            f = Frame(locator,
                      (locator.shift_horizontal + locator.block_size[0] // 2 + (i + 1) * locator.block_size[0],
                       locator.height - locator.shift_vertical - locator.block_size[1] // 2),
                      all_sprites)
            self.add(f)

        # Средняя часть рамки
        for i in range(locator.n_vertical - 2):
            f = Frame(locator,
                      (locator.width // 2 + locator.block_size[0] // 2,
                       locator.shift_vertical + locator.block_size[1] // 2 + (i + 1) * locator.block_size[1]),
                      all_sprites)
            self.add(f)

        # Часть рамки под Сложность
        for i in range(locator.n_horizontal - 15):
            f = Frame(locator,
                      (locator.shift_horizontal + locator.block_size[0] // 2 + (i + 1) * locator.block_size[0],
                       locator.shift_vertical + locator.block_size[1] // 2 + 6 * locator.block_size[1]),
                      all_sprites)
            self.add(f)

        # Часть рамки под Громкость
        for i in range(locator.n_horizontal - 15):
            f = Frame(locator,
                      (locator.shift_horizontal + locator.block_size[0] // 2 + (i + 1) * locator.block_size[0],
                       locator.shift_vertical + locator.block_size[1] // 2 + 12 * locator.block_size[1]),
                      all_sprites)
            self.add(f)


class GameFrame(pygame.sprite.Group):
    def __init__(self, locator, all_sprites):
        pygame.sprite.Group.__init__(self)

        # Левая часть рамки
        for i in range(locator.n_vertical):
            f = Frame(locator,
                      (locator.shift_horizontal + locator.block_size[0] // 2,
                       locator.shift_vertical + locator.block_size[1] // 2 + i*locator.block_size[1]),
                      all_sprites)
            self.add(f)

        # Правая часть рамки
        for i in range(locator.n_vertical):
            f = Frame(locator,
                      (locator.width - locator.shift_horizontal - locator.block_size[0] // 2,
                       locator.shift_vertical + locator.block_size[1] // 2 + i * locator.block_size[1]),
                      all_sprites)
            self.add(f)

        # Верхняя часть рамки
        for i in range(locator.n_horizontal - 2):
            f = Frame(locator,
                      (locator.shift_horizontal + locator.block_size[0] // 2 + (i + 1) * locator.block_size[0],
                       locator.shift_vertical + locator.block_size[1] // 2),
                      all_sprites)
            self.add(f)

        # Нижняя часть рамки
        for i in range(locator.n_horizontal - 2):
            f = Frame(locator,
                      (locator.shift_horizontal + locator.block_size[0] // 2 + (i + 1) * locator.block_size[0],
                       locator.height - locator.shift_vertical - locator.block_size[1] // 2),
                      all_sprites)
            self.add(f)

        # Средняя часть рамки
        for i in range(locator.n_vertical - 2):
            f = Frame(locator,
                      (locator.shift_horizontal + locator.block_size[0] // 2 + 5 * locator.block_size[0],
                       locator.shift_vertical + locator.block_size[1] // 2 + (i + 1) * locator.block_size[1]),
                      all_sprites)
            self.add(f)

        # Перегородки
        for i in range(locator.n_horizontal - 24):
            f = Frame(locator,
                      (locator.shift_horizontal + locator.block_size[0] // 2 + (i + 1) * locator.block_size[0],
                       locator.shift_vertical + locator.block_size[1] // 2 + 5 * locator.block_size[1]),
                      all_sprites)
            self.add(f)
        for i in range(locator.n_horizontal - 24):
            f = Frame(locator,
                      (locator.shift_horizontal + locator.block_size[0] // 2 + (i + 1) * locator.block_size[0],
                       locator.shift_vertical + locator.block_size[1] // 2 + 10 * locator.block_size[1]),
                      all_sprites)
            self.add(f)


# Один экземпляр рамки
class Frame(pygame.sprite.Sprite):
    def __init__(self, locator, position, all_sprites):
        pygame.sprite.Sprite.__init__(self)

        # Расчитываем размер экземпляра рамки
        size = locator.block_size

        # Инициализация параметров фона
        self.position = [size[0] // 2, size[1] // 2]
        images_dir = path.join(path.dirname(__file__), '..')
        images_dir = path.join(images_dir, "img")
        image = pygame.image.load(path.join(images_dir, "frame.png")).convert_alpha()
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.rect.center = position

        # Добавляем фон в группу спрайтов
        all_sprites.add(self)

    def update(self):
        pass
