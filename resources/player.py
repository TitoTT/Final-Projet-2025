#importamos mierdas
import pygame
import config

#nuestro PJ
class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.size = 20 #tamaño del pj, en pixeles po

#clase pa dibujar el pj en pantalla del game
    def draw(self, screen):
        pygame.draw.rect(screen, config.BLUE, rect:(self.x, self.y, self.size, self.size)) 

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
