from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemy1 = Character("Goblin", 20, 3)
    enemy2 = Character("Orc", 25, 4)

    enemies = [enemy1,enemy2]

    print(hero)
    for e in enemies:
        print(e)
    print()

    while hero.is_alive() and any(e.is_alive() for e in enemies):
        for e in enemies:
            if e.is_alive():
                hero.attack(e)
                break
        for e in enemies:
            if e.is_alive() and hero.is_alive():
                e.attack(hero)
        print(hero)
        for e in enemies:
            print(e)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"Enemies wins!")

if __name__ == "__main__":
    main()
