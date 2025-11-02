import random

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = int(hp)
        self.base_attack_power = int(attack_power)


    def attack(self, other):
        damage = int(round(random.uniform(0.3, 0.9) * self.base_attack_power))
        other.hp = max(0, other.hp - damage)
        print(f"{self.name} attacks {other.name} for {damage} damage!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp} HP"
