#importamos mierdas (de nuevo, ya me canse de importar, a este paso mejor hare todo junto en un solo archivo de 2k lineas de codigo xd)
import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=(100, 100, 100)):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class World:
    def __init__(self, level_data):
        self.platforms = pygame.sprite.Group()
        for data in level_data:
            platform = Platform(*data)
            self.platforms.add(platform)

    def draw(self, screen):
        self.platforms.draw(screen)
