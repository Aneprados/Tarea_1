# Añadir la clase Boss
# Importar las librerías necesarias
import pygame
import random
from Player import Player
try:
    from Opponent import Opponent  # Asegúrate de que Opponent.py esté en el mismo directorio o ajusta la ruta de importación
except ModuleNotFoundError as e:
    print(f"Error: {e}. Asegúrate de que el archivo Opponent.py exista y esté en el directorio correcto.")
from Boss import Boss
from Shot import Shot
from Game import Game
# Configuración de pantalla y colores
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

    
# Iniciar el juego
if __name__ == "__main__":
    game = Game()
    game.start()

    # Terminar pygame después de finalizar el juego
    pygame.quit()
    exit()
# Fin del código