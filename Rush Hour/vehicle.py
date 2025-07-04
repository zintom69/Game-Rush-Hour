MAX_COLS = 6
MAX_ROWS = 6

import pygame
from pygame.locals import *
'''
Vehicle:
    + index
    + position
    + length
    + direction
    + image
'''
class Vehicle:
    def __init__(self, index, pos, length, dir):

        if type(index) is int:
            self.index = index
            if self.index == 0:
                self.img_name = "./assets/red_car.png"
            else:
                if length == 2:
                    self.img_name = "./assets/car2.png"
                elif length == 3:
                    self.img_name = "./assets/car3.png"
                else:
                    raise Exception(length, "is not valid")
        else:
            raise Exception(index, "is not even a string")

        self.len = length

        if dir == "h" or dir == "v":
            self.dir = dir
        else:
            raise Exception("direction should be either 0 or 1")


        if type(pos) is list:
            if pos[0] >= 0 and  pos[0] <= MAX_COLS - 1 and \
                pos[1] >= 0 and pos[1] <= MAX_ROWS - 1:
                self.pos = [pos[0], pos[1]]
            else:
                raise Exception(pos, "is not in the valid number")


        self.image = pygame.image.load(self.img_name)
        self.image = pygame.transform.scale(self.image, (self.len * 100, 100))
        if self.dir == "v":
            self.image = pygame.transform.rotate(self.image, 90)

        






