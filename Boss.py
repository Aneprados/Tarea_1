from Opponent import Opponent

class Boss(Opponent):
    def __init__(self, x, y, speed):
        # Llama al constructor de la clase base Opponent
        super().__init__(x, y, speed * 2)  # El jefe final se mueve el doble de rápido

    def special_attack(self):
        # Implementa un ataque especial del jefe final
        print("El jefe final realiza un ataque especial devastador.")

    def reset(self):
        # Resetea el estado del jefe final
        super().reset()
        print("El jefe final ha sido reseteado.")
    def serialize(self):
        """"
        "Deserializa el estado del jefe final desde un diccionario."
        """
        data = super().serialize()
        data.update({
            "special_attack": self.special_attack
        })
        return data
    
    def deserialize(self, data):
        """"
        "Deserializa el estado del jefe final desde un diccionario."
        """
        super().deserialize(data)
        self.special_attack = data["special_attack"]

    def __str__(self):
        """
        Devuelve una representación en cadena del jefe final.
        :return: Una cadena que representa el estado del jefe final.
        """
        return f"Jefe Final en ({self.x}, {self.y}) con velocidad {self.speed}"
    
    def move(self):
        # Implementa la lógica de movimiento del jefe final
        print(f"El jefe final se mueve a ({self.x}, {self.y})")
    def hit_target(self):
        # Implementa la lógica para verificar si el jefe final golpea un objetivo
        print("El jefe final ha golpeado un objetivo.")


    def take_damage(self, damage):
        """
        Reduce la salud del jefe final al recibir daño.
        :param damage: Cantidad de daño recibido.
        """
        self.health -= damage
        print(f"El jefe final recibe {damage} de daño. Salud restante: {self.health}")
        if self.health <= 0:
            self.defeated()

    def defeated(self):
        """
        Lógica para manejar cuando el jefe final es derrotado.
        """
        print("¡El jefe final ha sido derrotado!")

    def is_final_boss(self):
        """
        Indica si este oponente es el jefe final.
        :return: True, ya que esta clase representa al jefe final.
        """
        return True
    
    def is_boss(self):
        """
        Returns True if the character is a boss, False otherwise.
        """
        return hasattr(self, "is_final_boss") and self.is_final_boss()

    def defeat_enemy(self):
        """
        Handles logic when the player defeats an enemy.
        If an enemy is defeated, a final boss is spawned.
        """
        # Example logic to spawn a boss
        boss = Boss(self.x, self.y, self.speed)  # Create a boss with the current position and speed
        boss.is_final_boss = True  # Mark this character as the final boss
        return boss

