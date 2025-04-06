from Chatter import Character, Entity  # Asegúrate de que Entity esté disponible
from Shot import Shot  # Importing here to avoid circular imports
import time


class Player(Character):
    def __init__(self, name, x=0, y=0, image="default_player_image.png", score=0, lives=3):
        super().__init__(name)
        Entity.__init__(self, x, y, image)  # Explicitly call Entity's __init__ with required arguments
        self.score = score
        self.lives = lives

    def __str__(self):
        return f"Player {self.name} at ({self.x}, {self.y}) with score {self.score} and lives {self.lives}"

    def move(self, direction):
        """
        Moves the player in the specified direction.
        :param direction: A string indicating the direction ('up', 'down', 'left', 'right').
        """
        valid_directions = ['up', 'down', 'left', 'right']
        if direction not in valid_directions:
            print(f"Invalid direction: {direction}. Valid directions are: {valid_directions}")
            return

        # Example logic for movement
        if direction == 'up':
            self.y -= 1
            print(f"{self.name} moves up to ({self.x}, {self.y}).")
        elif direction == 'down':
            self.y += 1
            print(f"{self.name} moves down to ({self.x}, {self.y}).")
        elif direction == 'left':
            self.x -= 1
            print(f"{self.name} moves left to ({self.x}, {self.y}).")
        elif direction == 'right':
            self.x += 1
            print(f"{self.name} moves right to ({self.x}, {self.y}).")

    def shoot(self):
        """
        Creates a shot fired by the player.
        """
        shot = Shot(self.name, is_enemy_shot=False)
        print(f"{self.name} shoots a shot!")
        return shot

    def collide(self, other_entity):
        """
        Handles collision logic with another entity.
        :param other_entity: The entity this player collides with.
        """
        if hasattr(other_entity, "is_enemy_shot") and other_entity.is_enemy_shot:
            self.lives -= 1
            print(f"{self.name} was hit by an enemy shot! Lives remaining: {self.lives}")
            if self.lives <= 0:
                print(f"Game Over for {self.name}!")
        elif hasattr(other_entity, "is_power_up") and other_entity.is_power_up:
            self.score += other_entity.value
            print(f"{self.name} collected a power-up! Score increased by {other_entity.value}. Total score: {self.score}")
        elif hasattr(other_entity, "is_obstacle") and other_entity.is_obstacle:
            self.lives -= 1
            print(f"{self.name} collided with an obstacle! Lives remaining: {self.lives}")
            if self.lives <= 0:
                print(f"Game Over for {self.name}!")

    def reset(self):
        # Reset player-specific attributes
        self.score = 0
        self.lives = 3
        self.x = 0
        self.y = 0
        print(f"{self.name} has been reset to position ({self.x}, {self.y}).")

    def respawn(self):
        """
        Respawns the player after being hit, if lives remain.
        """
        if self.lives > 0:
            print(f"{self.name} is respawning...")
            time.sleep(2)  # Simulate a brief delay for respawning
            print(f"{self.name} has respawned at position ({self.x}, {self.y})!")
        else:
            print(f"{self.name} cannot respawn. No lives remaining.")
