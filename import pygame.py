import pygame
from Game import Game

# Inicializar pygame
pygame.init()

# Configurar la ventana del juego
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego")
clock = pygame.time.Clock()

if __name__ == "__main__":
    game = Game()
    game.start()
    game.spawn_player("Player1")  # Asegúrate de que Player1 tenga valores predeterminados para x, y e image
    game.spawn_opponent(is_star=True)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizar el estado del juego
        game.update_opponent()
        game.update_player()
        if game.player:
            game.player.shoot()
        if game.opponent:
            game.opponent.shoot()
        game.update()

        # Dibujar en la pantalla
        screen.fill((0, 0, 0))  # Fondo negro
        # Aquí puedes agregar lógica para dibujar entidades del juego
        # Por ejemplo: game.draw(screen)

        pygame.display.flip()
        clock.tick(60)  # Limitar a 60 FPS

    game.end_game()
    game.reset()
    pygame.quit()