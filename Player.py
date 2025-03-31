import pygame
from Shot import Shot
from Chatter import Character  # Assuming Character is defined in Character.py


class Player(Character):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)  # Call the parent class constructor
        self.lives = 3
        self.score = 0  # Initialize score to 0

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5
        if keys[pygame.K_UP]:
            self.y -= 5
        if keys[pygame.K_DOWN]:
            self.y += 5

    def shoot(self):
        # Create a shot from the player's position
        return Shot(self.x + self.image.get_width() // 2, self.y)
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def reset_position(self):
        # Reset player position to the center of the screen
        self.x = (screen.get_width() - self.image.get_width()) // 2
        self.y = screen.get_height() - self.image.get_height() - 10  # 10 pixels from the bottom of the screen
    def is_off_screen(self):
        # Check if the player is off screen
        return self.x < 0 or self.x > screen.get_width() or self.y < 0 or self.y > screen.get_height()
    def collide(self):
        return super().collide()
