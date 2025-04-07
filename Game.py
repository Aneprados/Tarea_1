from Player import Player


class Game:
    """
    Main class to handle the game logic.
    """
    def __init__(self):
        self.is_running = False
        self.player = None

    def start(self):
        """
        Starts the game.
        """
        self.is_running = True
        print("Game started!")

    def end_game(self):
        """
        Ends the game.
        """
        self.is_running = False
        print("Game ended!")

    def reset(self):
        """
        Resets the game state.
        """
        self.player = None
        print("Game reset!")

    def initialize_player(self, player_name="DefaultPlayer"):
        """
        Initializes the player with a given name.
        :param player_name: Name of the player.
        """
        self.player = Player(name=player_name)
        self.player.lives = 3
        self.player.score = 0
        print(f"Player {self.player.name} initialized with {self.player.lives} lives and score {self.player.score}.")

    def spawn_player(self, player_name="DefaultPlayer"):
        """
        Spawns a player in the game.
        :param player_name: Name of the player.
        """
        if self.is_running:
            self.initialize_player(player_name)
            print(f"Player {self.player.name} spawned!")
        else:
            print("Game is not running. Cannot spawn player.")

    def update_player(self):
        """
        Updates the player's state.
        """
        if self.player:
            print(f"Updating player {self.player.name}...")
        else:
            print("No player to update.")

    def update_opponent(self):
        """
        Updates the opponent's state (placeholder).
        """
        print("Updating opponent (placeholder).")

    def update(self):
        """
        Updates the general game state.
        """
        print("Game state updated.")

    def spawn_opponent(self, is_star=False):
        """
        Spawns an opponent in the game.
        :param is_star: Boolean indicating if the opponent is a star.
        """
        print(f"Opponent spawned. Is star: {is_star}")      
    
    def spawn_player(self, player_name, x=100, y=100, image="player_image.png"):
        """
        Spawns a player in the game with default or specified attributes.
        :param player_name: Name of the player.
        :param x: X-coordinate of the player.
        :param y: Y-coordinate of the player.
        :param image: Image associated with the player.
        """
        if self.is_running:
            self.player = Player(name=player_name, x=x, y=y, image=image)
            print(f"Player {self.player.name} spawned at ({x}, {y}) with image '{image}'!")
        else:
            print("Game is not running. Cannot spawn player.")

    # Añadimos un método para manejar oponentes
    def spawn_opponent(is_star=False):
        """
        Método temporal para manejar la creación de un oponente.
        :param is_star: Indica si el oponente es especial.
        """
        if is_star:
            print("Star opponent spawned!")
        else:
            print("Regular opponent spawned!")

    # Llamamos al método para crear un oponente
    spawn_opponent(is_star=True)

    def spawn_opponent(self, is_star=False):
        """
        Spawns an opponent in the game.
        :param is_star: Boolean indicating if the opponent is a star.
        """
        print(f"Opponent spawned. Is star: {is_star}")   