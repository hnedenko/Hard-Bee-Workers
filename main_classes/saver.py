class Saver:
    def __init__(self, ):
        pass

    def load_state(self):
        readed_dict = dict()
        with open('sav/save.sav') as inp:
            for i in inp.readlines():
                key, val = i.strip().split(':')
                readed_dict[key] = val
        return readed_dict

    def save_state(self, money, level_n_bees, level_speed_bees, level_money_profit, time, timestamp):
        readed_dict = dict()
        with open('sav/save.sav') as inp:
            for i in inp.readlines():
                key, val = i.strip().split(':')
                readed_dict[key] = val
        readed_dict["money"] = money
        readed_dict["level_n_bees"] = level_n_bees
        readed_dict["level_speed_bees"] = level_speed_bees
        readed_dict["level_money_profit"] = level_money_profit
        readed_dict["time"] = time
        readed_dict["timestamp"] = timestamp
        with open('sav/save.sav', 'w') as out:
            for key, val in readed_dict.items():
                out.write('{}:{}\n'.format(key, val))

    def save_difficulty(self, difficulty):
        readed_dict = dict()
        with open('sav/save.sav') as inp:
            for i in inp.readlines():
                key, val = i.strip().split(':')
                readed_dict[key] = val
        readed_dict["difficulty"] = difficulty
        with open('sav/save.sav', 'w') as out:
            for key, val in readed_dict.items():
                out.write('{}:{}\n'.format(key, val))

    def save_volume(self, volume):
        readed_dict = dict()
        with open('sav/save.sav') as inp:
            for i in inp.readlines():
                key, val = i.strip().split(':')
                readed_dict[key] = val
        readed_dict["volume"] = volume
        with open('sav/save.sav', 'w') as out:
            for key, val in readed_dict.items():
                out.write('{}:{}\n'.format(key, val))

    def save_sound_mode(self, mode):
        readed_dict = dict()
        with open('sav/save.sav') as inp:
            for i in inp.readlines():
                key, val = i.strip().split(':')
                readed_dict[key] = val
        readed_dict["sound_mode"] = mode
        with open('sav/save.sav', 'w') as out:
            for key, val in readed_dict.items():
                out.write('{}:{}\n'.format(key, val))
