import random
from goblin import Goblin
from hero import Hero
from boss import King


def main():

    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Aragorn")

    # Create goblins and king ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(3)]
    goblin_king = King("Goblin King")
    # Keep track of how many goblins were defeated
    defeated_goblins = 0

    rounds_survived = 0
    total_damage_dealt = 0
    # Battle Loop
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        rounds_survived += 1

        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)
        total_damage_dealt += damage
        hero.special_chance()

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)

    # Determine outcome
    if hero.is_alive():
        print("\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print("\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")
        rounds_survived -= 1

    # boss battle
    print("BOSS TIME!!!")
    while hero.is_alive() and goblin_king.is_alive():
        damage = hero.strike()
        total_damage_dealt += damage
        goblin_king.take_damage(damage)
        if goblin_king.is_alive():
            goblin_king.intimidation()
            damage = goblin_king.attack()
            print(f"Goblin King attacks for {damage} damage")
            hero.receive_damage(damage)
        else:
            print("YOU HAVE DEFEATED THE KING")
        if not (hero.is_alive()):
            print("YOU HAVE BEEN ANNIHILATED")

    print("\nBattle Summary:" + "\nTotal Damage Dealt: " + str(total_damage_dealt) + "\nRounds Survived: " + str(rounds_survived))
    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")


if __name__ == "__main__":
    main()
