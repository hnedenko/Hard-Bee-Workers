import pygame
import random
from os import path
from main_classes import saver


class SoundPlayer:
    def __init__(self, ):
        pygame.mixer.init()
        # Сохраняемые настройки звука
        self.saver = saver.Saver().load_state()
        self.mode = self.saver["sound_mode"]
        self.volume = self.saver["volume"]

        # Папка со звуками
        self.dir = path.join(path.dirname(__file__), '../snd')

        # Загрузка аудио
        if self.mode == "winni":
            pygame.mixer.music.load(path.join(self.dir, 'winni_00.ogg'))
        elif self.mode == "SW":
            pygame.mixer.music.load(path.join(self.dir, 'SW_impersky_marsh.ogg'))
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(int(self.volume)/100)

    def set_volume(self, volume):
        self.volume = volume
        pygame.mixer.music.set_volume(int(self.volume) / 100)
