import random
import pygame   
# from Shot import Shot  # Elimina si Shot no es utilizado en este archivo
# Fallback implementation for Opponent
class Opponent:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move(self):
        pass  # Implement basic movement logic if needed
# from Game import Game  # Elimina si Game no es utilizado en este archivo

# Define SCREEN_HEIGHT y SCREEN_WIDTH globalmente o impórtalos desde un módulo de constantes
SCREEN_HEIGHT = 600  # Valor de ejemplo
SCREEN_WIDTH = 800   # Valor de ejemplo

# Clase Boss (heredando de Opponent)
class Boss(Opponent):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.lives = 5  # El jefe tiene más vidas
        self.speed = 6  # Establecer la velocidad del jefe (puedes ajustar este valor)

    def move(self):
        # Movimiento del jefe, mueve hacia abajo
        self.y += self.speed
        # Si el jefe ha llegado a la parte inferior de la pantalla, lo reseteamos en la parte superior
        if self.y > SCREEN_HEIGHT:
            self.y = -self.image.get_height()
            self.x = random.randint(0, SCREEN_WIDTH - self.image.get_width())

