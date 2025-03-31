from entity import Entity

class Character(Entity):
    def __init__(self, lives):
        super().__init__()
        self.lives = lives
        self.is_alive = lives > 0

    def move(self, direction):
        """
        Moves the character in the specified direction.
        :param direction: A string indicating the direction (e.g., 'up', 'down', 'left', 'right').
        """
        print(f"Character is moving {direction}.")

    def shoot(self):
        """
        Simulates the character shooting.
        """
        print("Character is shooting.")

    def collide(self):
        """
        Handles collision logic. Reduces lives and updates is_alive status.
        """
        if self.lives > 0:
            self.lives -= 1
            print(f"Character collided! Lives remaining: {self.lives}")
        self.is_alive = self.lives > 0
        if not self.is_alive:
            print("Character is no longer alive.")

    def reset_position(self):
        """
        Resets the character's position to the starting point.
        """
        print("Character position reset.")
        self.x = 0
        self.y = 0
        