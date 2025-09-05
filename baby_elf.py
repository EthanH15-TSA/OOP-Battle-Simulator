from enemy import Enemy

class baby_elf(Enemy):
    #a new special ability
    def cry():
        print("wahh wahhh")

    #overriding take damage
    def take_damage(self, damage):
        print("Why are you attacking a baby, YOU MONSTER!!!!")
        return super().take_damage(damage)