from enemy import Enemy


class boss(Enemy):

    def __init__(self, name):
        super().__init__(name)
        self.health = 200

    def intimidation():
        print("Puny Hero")

    def take_damage(self, damage):
        print("I could barely feel that")
        return super().take_damage(damage)