from character import Character, Hero
from typing import List

def startEncounter(hero: Character, enemyList: List[Character]):
    while (not hero.killed and len(enemyList) > 0):
        killed = hero.takeTurn(enemyList)
        if killed[0] == 1:
            enemy = killed[1]
            enemyList.remove(enemy)
        for enemy in enemyList:
            enemy.attackEnemy(hero)

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
    enemy2 = Character("Goblin2", 5, 8)
    startEncounter(mainGuy, [enemy1, enemy2])