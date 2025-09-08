from enemy import Enemy


class King(Enemy):

    def __init__(self, name):
        super().__init__(name)
        self.health = 250
        self.attack_power = 20

    def attack(self):
        if self.health < 100:
            self.attack_power = 70
        return self.attack_power

    def intimidation(self):
        print("Puny Hero")

    def take_damage(self, damage):
        if damage != 200:
            print("I could barely feel that")
        return super().take_damage(damage)