import pygame
from Shot import Shot


class Player:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.lives = 3

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5
        if keys[pygame.K_UP]:
            self.y -= 5
        if keys[pygame.K_DOWN]:
            self.y += 5

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def shoot(self):
        # Crea un disparo desde la posición del jugador
        return Shot(self.x + self.image.get_width() // 2, self.y)
