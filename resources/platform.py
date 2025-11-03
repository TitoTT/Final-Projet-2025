#importamos mierdas (de nuevo, ya me canse de importar, a este paso mejor hare todo junto en un solo archivo de 2k lineas de codigo xd)
import pygame
import config


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def draw(self, screen):
        