import pygame
from resources.platform import Platform

class World:
    def __init__(self, data):
        self.platform_list = []
        
        # Crear plataformas desde los datos
        for platform_data in data:
            x, y, width, height = platform_data
            platform = Platform(x, y, width, height)
            self.platform_list.append(platform)
    
    def draw(self, surface):
        # Dibujar todas las plataformas
        for platform in self.platform_list:
            platform.draw(surface)
