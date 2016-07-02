# coding:utf8
import random


class Individual():

    def __init__(self, envi):
        position = False

        while position == False:
            self.x = random.randrange(envi.width)
            self.y = random.randrange(envi.hight)

            position = envi.envi[self.y][self.x] == 0

        if self.x % 2 == 0:
            self.neighbor = envi.envi[self.y][self.x + 1]
        else:
            self.neighbor = None
