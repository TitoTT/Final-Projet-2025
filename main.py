#AQUI IMPORTAMOS VARIAS MIERDAS
import config
import pygame
import sys
from resources.platform import Platform
from resources.platform import World 
from resources.player import Player


#inicializar el Pitogame
pygame.init()

#este inicializa la ventana
Ventana = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Plataformero basico")

#pa controlar los FPS
clock = pygame.time.Clock()

#la data del level we(x, y, ancho, alto)

level_data = [
(0, 550, 800, 50), #va a ser el piso principal
(200, 450, 100, 20), #primera plataforma
(400, 350, 120, 20), #segunda plataforma
(600, 250, 100, 20), #tercera plataforma

]
#pa crear el mundo con las plataformas
world = World(level_data)
player = Player(100, 500)


#bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #logica del player
    player.update(world.platforms)


    #fondo del cielo = azul
    Ventana.fill((135, 206, 235))
    
    #dibujar plataformas
    world.draw(Ventana)
    
    player.draw(Ventana)


    #actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

# Limpiar y salir
pygame.quit()
sys.exit()