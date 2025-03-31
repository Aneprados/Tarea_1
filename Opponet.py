
import pygame

class Opponent:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move(self):
        self.y += 3  # Moverse hacia abajo

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def collide(self, shot):
        return self.image.get_rect(topleft=(self.x, self.y)).colliderect(shot.image.get_rect(topleft=(shot.x, shot.y)))
