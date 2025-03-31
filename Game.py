#De aqui sale todo el juego
import pygame
import random
from Player import Player
import os
# Removed unused import

opponent_path = os.path.join(os.path.dirname(__file__), "Opponent.py")
if os.path.exists(opponent_path):
    from Opponent import Opponent
else:
    raise ImportError(f"'Opponent.py' not found at {opponent_path}. Please create or place the file in the correct directory.")

from Boss import Boss


# Clase Game
class Game:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 800, 600
        self.FPS = 60
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Shooting Game")
        self.clock = pygame.time.Clock()
        self.player = Player(400, 500, pygame.Surface((50, 50)))
        self.player.image.fill(self.WHITE)
        self.opponents = [Opponent(random.randint(0, self.SCREEN_WIDTH - 50), random.randint(-100, -40), pygame.Surface((50, 50))) for _ in range(5)]
        for opponent in self.opponents:
            opponent.image.fill((255, 0, 0))
        self.shots = []
        self.score = 0
        self.boss = None  # Inicialmente no hay jefe final
        self.is_running = True

    def start(self):
        while self.is_running:
            self.update()

    def update(self):
        self.screen.fill(self.BLACK)
        keys = pygame.key.get_pressed()

        # Movimiento del jugador
        self.player.move(keys)
        self.player.draw(self.screen)

        # Movimiento de los enemigos
        for opponent in self.opponents:
            opponent.move()
            opponent.draw(self.screen)

        # Movimiento del jefe final
        if self.boss:
            self.boss.move()
            self.boss.draw(self.screen)

        # Movimiento de los disparos
        for shot in self.shots[:]:
            shot.move()
            shot.draw(self.screen)
            if shot.y < 0 or shot.y > self.SCREEN_HEIGHT:
                self.shots.remove(shot)

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.shots.append(self.player.shoot())

        # Detección de colisiones
        for shot in self.shots[:]:
            for opponent in self.opponents[:]:
                if shot.collide(opponent):
                    self.shots.remove(shot)
                    self.opponents.remove(opponent)
                    self.score += 1
                    if not self.opponents and not self.boss:  # Si no quedan enemigos, aparece el jefe
                        self.boss = Boss(random.randint(0, self.SCREEN_WIDTH - 50), -100, pygame.Surface((100, 100)))
                        self.boss.image.fill((0, 255, 0))

            if self.boss and shot.collide(self.boss):
                self.shots.remove(shot)
                self.boss.lives -= 1
                if self.boss.lives <= 0:
                    self.boss = None
                    self.end_game()  # Mostrar mensaje de victoria antes de terminar el juego

        # Mostrar puntuación y vidas
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, self.WHITE)
        lives_text = font.render(f"Lives: {self.player.lives}", True, self.WHITE)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 50))

        pygame.display.flip()
        self.clock.tick(self.FPS)

    def end_game(self):
        font = pygame.font.Font(None, 72)
        if self.boss is None and self.player.lives > 0:
            message = "You Win!"
        else:
            message = "Game Over"
        text = font.render(message, True, self.WHITE)
        self.screen.fill(self.BLACK)
        self.screen.blit(text, (self.SCREEN_WIDTH // 2 - text.get_width() // 2, self.SCREEN_HEIGHT // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        self.is_running = False  # Terminamos el juego después de mostrar el mensaje
