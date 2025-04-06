import pygame

# Asegúrate de que las clases y métodos como Game, spawn_player, etc., estén definidos correctamente
from game_script import Game  # Importa tu clase Game desde otro archivo si es necesario

# Inicialización de pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))  # Cambia el tamaño de la ventana según sea necesario
clock = pygame.time.Clock()

if __name__ == "__main__":
    game = Game()
    game.start()
    game.spawn_player("Player1")
    game.spawn_opponent(is_star=True)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizar el estado del juego
        game.update_opponent()
        game.update_player()
        game.player.shoot()
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
