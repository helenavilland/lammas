import pygame 
from pygame.math import Vector2


class Tree:

    def __init__(self, start, direction, length):
        self.start = start
        self.direction = Vector2(direction)
        self.length = length
        self.branches = []

    def render(self, screen):
        end_pos = (self.start[0] + self.direction.x * self.length, 
                   self.start[1] + self.direction.y * self.length)
        pygame.draw.line(screen, (100, 100, 20), self.start, end_pos)
