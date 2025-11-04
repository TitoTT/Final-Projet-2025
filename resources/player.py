import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Movimiento
        self.vel_y = 0
        self.speed = 5
        self.jump_force = -15
        self.gravity = 0.8

        # Estado
        self.on_ground = False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_force
            self.on_ground = False

    def apply_gravity(self):
        self.vel_y += self.gravity
        if self.vel_y > 10:
            self.vel_y = 10  # límite de velocidad
        self.rect.y += self.vel_y

    def horizontal_collision(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                # Si viene de la derecha
                if self.speed > 0 and self.rect.right > platform.rect.left:
                    self.rect.right = platform.rect.left
                # Si viene de la izquierda
                elif self.speed < 0 and self.rect.left < platform.rect.right:
                    self.rect.left = platform.rect.right

    def vertical_collision(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:  # cayendo
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:  # saltando
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0

    def update(self, platforms):

        self.handle_input()

        old_x = self.rect.x  # guardamos posición anterior

        # Movimiento horizontal
        keys = pygame.key.get_pressed()
        dx = 0
        if keys[pygame.K_LEFT]:
            dx = -self.speed
        if keys[pygame.K_RIGHT]:
            dx = self.speed
        self.rect.x += dx

        # Colisiones horizontales
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if dx > 0:  # hacia la derecha
                    self.rect.right = platform.rect.left
                elif dx < 0:  # hacia la izquierda
                    self.rect.left = platform.rect.right

        # Movimiento vertical
        self.vel_y += self.gravity
        if self.vel_y > 10:
            self.vel_y = 10
        self.rect.y += self.vel_y

        # Colisiones verticales
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:  # cayendo
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:  # saltando
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
