import random


class Hero:

    def __init__(self, name):
        self.name = name
        self.health = 200
        self.attack_power = random.randint(2, 50)

    def strike(self):
        crit_chance = random.randint(1, 10)
        if crit_chance == 1:
            print("Critical Hit!!!!")
            return 150
        else:
            return random.randint(1, self.attack_power)

    # chance of hero getting a full heal
    def special_chance(self):
        special_chance = random.randint(1, 20)
        if special_chance == 1:
            self.health = 200
            print("Special activated: Full Heal!!!")

    def receive_damage(self, damage):
        reduce_chance = random.randint(1, 50)
        if self.health < 100:
            reduce_chance += 5
        if reduce_chance > 10:
            damage *= 0.5
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0
