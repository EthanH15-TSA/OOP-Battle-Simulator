from enemy import Enemy


class King(Enemy):

    def __init__(self, name):
        super().__init__(name)
        self.health = 300
        self.attack_power = 20

    def attack(self):
        if self.health < 50
            self.attack_power = 50
        return self.attack_power

    def intimidation():
        print("Puny Hero")

    def take_damage(self, damage):
        print("I could barely feel that")
        return super().take_damage(damage)