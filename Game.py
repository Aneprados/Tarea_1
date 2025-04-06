class Player:
    """
    A simple Player class to represent a player in the game.
    """
    def __init__(self, name):
        self.name = name
        self.lives = 0
        self.score = 0

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
