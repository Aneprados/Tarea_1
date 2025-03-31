# Clase Shot
import pygame

class Shot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 10
        self.color = (255, 255, 255)  # Define WHITE as an RGB tuple
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)

    def move(self):
        self.y -= 5  # The shot moves upward

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def collide(self, opponent):
        shot_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        opponent_rect = pygame.Rect(opponent.x, opponent.y, opponent.image.get_width(), opponent.image.get_height())
        return shot_rect.colliderect(opponent_rect)