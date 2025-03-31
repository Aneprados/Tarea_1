
import pygame
from Chatter import Character  # Assuming Character is defined in Character.py
class Character:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Opponent(Character):
    def __init__(self, x, y, image, is_star=False):
        super().__init__(x, y, image)
        self.is_star = is_star

    def move(self):
        self.y += 3  # Moverse hacia abajo

    def shoot(self, bullet_image):
        # Crear un disparo desde la posición del oponente
        return Bullet(self.x + self.image.get_width() // 2, self.y + self.image.get_height(), bullet_image)

    def collide(self, shot):
        return self.image.get_rect(topleft=(self.x, self.y)).colliderect(shot.image.get_rect(topleft=(shot.x, shot.y)))

class Bullet:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move(self):
        self.y += 5  # Moverse hacia abajo

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
