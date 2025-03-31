class Entity:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        # Placeholder for drawing logic
        print(f"Drawing entity at ({self.x}, {self.y}) with image {self.image}")
    
    def collide(self, other):
        # Placeholder for collision detection logic
        return False    
    
    def get_rect(self):
        # Placeholder for getting the rectangle of the entity for collision detection
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
    
    def reset_position(self):
        # Placeholder for resetting the position of the entity
        self.x = 0
        self.y = 0
    
    def is_off_screen(self):
        # Placeholder for checking if the entity is off screen
        return self.x < 0 or self.x > 800 or self.y < 0 or self.y > 600
    
    def update(self):
        # Placeholder for updating the entity's state
        pass

    