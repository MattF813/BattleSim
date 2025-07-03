from character import Character, Hero

if __name__ == '__main__':
    charName = input("Welcome to Battle Simulator! Please enter your name: ")
    mainGuy = ""
    while (mainGuy == ""):
        print("Please select a class.")
        classType = input("Hero : ")
        if (classType.casefold() == 'Hero'.casefold()):
            mainGuy = Hero(charName, 20, 5, 10)
        else:
            print("Class not found. Please try again")
    print("" + mainGuy.name + " wakes up in a dark cave. A fearsome goblin stands in front of them, ready for battle!")
    enemy1 = Character("Goblin", 10, 5)
    while (not mainGuy.killed and not enemy1.killed):
        print("" + mainGuy.name + "'s turn! Select one of the following options:")
        choice = input("1. Attack \n")
        if choice == str(1):
            mainGuy.attackEnemy(enemy1)
            if (enemy1.killed):
                break
        print("Enemy turn!")
        enemy1.attackEnemy(mainGuy)