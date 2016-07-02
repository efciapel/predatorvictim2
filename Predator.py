# coding:utf8
from Individual import Individual

class Predator(Individual):

    def __init__(self, envi):
        Individual.__init__(self, envi)
        envi.set_individual(self.x, self.y, ind='predator')
