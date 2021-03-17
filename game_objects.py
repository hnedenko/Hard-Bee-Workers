from main_classes import menu_objects
from main_classes import game_process_objects
from main_classes import settings_objects
from main_classes import locator
from main_classes import level_upper


class GameObject:
    def __init__(self, screen, width, height, sound_player):
        # Локатор, информация о новых уровнях и скрин для последуещего размещения объектов
        self.locator = locator.Locator(width, height)
        self.level_upper = level_upper.LevelUpper()
        self.screen = screen
        self.sound_player = sound_player

        # Текущий режим
        self.current_objects = menu_objects.MenuObjects(self.screen, self.locator, self.level_upper)

        # Выход из игры
        self.exit = False

    def update(self):
        # Переходим в новый режим, если надо
        if self.current_objects.go_to == "MENU":
            # Обновление текущего состояние
            self.current_objects.save_state()
            self.level_upper = level_upper.LevelUpper()
            self.current_objects = menu_objects.MenuObjects(self.screen,
                                                            self.locator,
                                                            self.level_upper)
            self.current_objects.load_state()
        elif self.current_objects.go_to == "GAME_LOAD":
            # Обновление текущего состояние
            self.current_objects.save_state()
            self.level_upper = level_upper.LevelUpper()
            self.current_objects = game_process_objects.GameProcessObjects(self.screen,
                                                                           self.locator,
                                                                           self.level_upper,
                                                                           self.sound_player,
                                                                           "LOAD")
        elif self.current_objects.go_to == "GAME_NEW":
            # Обновление текущего состояние
            self.current_objects.save_state()
            self.level_upper = level_upper.LevelUpper()
            self.current_objects = game_process_objects.GameProcessObjects(self.screen,
                                                                           self.locator,
                                                                           self.level_upper,
                                                                           self.sound_player,
                                                                           "NEW")
            self.current_objects.load_state()

        elif self.current_objects.go_to == "SETTINGS":
            # Обновление текущего состояние
            self.current_objects.save_state()
            self.current_objects = settings_objects.SettingsObjects(self.screen,
                                                                    self.locator,
                                                                    self.level_upper,
                                                                    self.sound_player)
            self.current_objects.load_state()
        else:
            # Обновляем состояние объектов для текущего режима
            self.current_objects.update()

        # Выход из игры, если надо
        if self.current_objects.exit:
            self.exit = True

    def draw(self):
        # Отрисовываем объекты текущего режима
        self.current_objects.draw()
