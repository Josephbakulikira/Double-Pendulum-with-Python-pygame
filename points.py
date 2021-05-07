import pygame

class Points:
    def __init__(self, x, y, surface,colors,coordinates):
        self.x = x
        self.y = y
        self.surface = surface
        self.colors = colors
        self.coordinates = coordinates
    def draw(self):
        if len(self.coordinates) > 2:
            pygame.draw.lines(self.surface, self.colors, False, self.coordinates, 4)
