import math
from main_classes import saver


class LevelUpper:
    def __init__(self, ):
        self.saver = saver.Saver()
        self.difficulty = int(self.saver.load_state()["difficulty"])

        self.number = [1, 2, 3, 4, 5,
                       6, 7, 8, 9, 10,
                       12, 14, 16, 18, 20,
                       22, 24, 26, 28, 30,
                       33, 36, 40, 45, 50]
        self.speed = [5, 6, 7, 8, 9,
                      10, 11, 12, 13, 14,
                      15, 16, 17, 18, 19,
                      20, 21, 22, 23, 24,
                      25, 26, 27, 28, 30]
        self.profit = [1, 2, 3, 4, 5,
                       7, 9, 10, 20, 30,
                       40, 50, 75, 100, 150,
                       200, 250, 300, 350, 400,
                       500, 600, 700, 800, 999]

        self.number_cost = [1]
        self.speed_cost = [1]
        self.profit_cost = [1]
        for i in range(24):
            add_n = math.ceil(self.number_cost[i]*self.difficulty*1.1)
            add_s = math.ceil(self.speed_cost[i]*self.difficulty*1.2)
            add_p = math.ceil(self.profit_cost[i]*self.difficulty*1.3)

            self.number_cost.append(add_n)
            self.speed_cost.append(add_s)
            self.profit_cost.append(add_p)
