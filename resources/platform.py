#importamos mierdas (de nuevo, ya me canse de importar, a este paso mejor hare todo junto en un solo archivo de 2k lineas de codigo xd)
import pygame
import config


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height


    def draw(self, screen):
        pass