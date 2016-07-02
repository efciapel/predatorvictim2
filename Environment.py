#coding:utf-8
import numpy

class Environment(object):

    predators = 0
    victims = 0

    def __new__(type):
        if not '_instancja' in type.__dict__:
            type._instancja = object.__new__(type)

        return type._instancja

    def set_size(self, x, y):
        self.hight = y
        self.width = x
        self.size = self.hight * self.width
        self.envi = numpy.zeros((self.hight, self.width))

    def set_individual(self, x, y, ind):
        if ind == 'victim':
            self.envi[y][x] = 2
        elif ind == 'predator':
            self.envi[y][x] = 1
        elif ind == 'empty':
            self.envi[y][x] = 0

    def observator(self):
        for i in self.envi:
            for j in i:
                if j == 1:
                    self.predators = self.predators + 1
                elif j == 2:
                    self.victims = self.victims + 1

    def envi_clear(self):
        self.envi = numpy.zeros((self.hight, self.width))
