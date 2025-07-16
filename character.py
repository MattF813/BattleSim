from typing import List

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        self.killed = False
    
    def attackEnemy(self, enemy):
        print("" + self.name + " has attacked " + enemy.name + "!")
        return enemy.takeDamage(self.attack)
    
    def takeDamage(self, enemyAttack):
        self.health -= enemyAttack
        print("The attack dealt " + str(enemyAttack) + " damage!")
        if (self.health <= 0):
            print("Fatal blow! " + self.name + " has perished.")
            self.killed = True

class Hero(Character): 
    def __init__(self, name, health, attack, magic):
        super().__init__(name, health, attack)
        self.healthMax = health
        self.magicMax = magic
        self.magic = magic
        self.lvl = 1

    def attackEnemy(self, enemyList: List[Character]):
        enemyNum = len(enemyList)
        enemyChoice = enemyNum
        while (True):
            if (enemyNum == 1):
                enemyChoice = 0
                break
            enemyChoice = input("There are " + str(enemyNum) + " enemies. Please select your target by entering a number from 1-" + str(enemyNum) + ": ")
            enemyChoice = int(enemyChoice)
            if (enemyChoice < 0 or enemyChoice > len(enemyList)):
                print("Number chosen is not a valid target. Please try again.")
            else:
                enemyChoice -= 1
                break
        enemy = enemyList[enemyChoice]
        super().attackEnemy(enemy)
        if enemy.killed:
            self.magic = self.magicMax
            self.health = self.healthMax
            self.lvl += 1
            print("Congratulations! " + self.name + " has reached level " + str(self.lvl) + ". Health and Mana have been restored!")
            return [1, enemy]
        return [0, enemy]
    def takeTurn(self, enemyList: List[Character]):
        choice = input("Please select from the following options: \n1. Attack \n")
        if choice == "1":
            return self.attackEnemy(enemyList)


if __name__ == '__main__':
    mainGuy = Hero("Hero", 20, 5, 10)
    print(mainGuy.name)
    print(mainGuy.health)
    print(mainGuy.attack)
    print(mainGuy.magic)
    enemy = Character("Enemy", 10, 8)
    print(enemy.name)
    print(enemy.health)
    print(enemy.attack)
    mainGuy.attackEnemy(enemy)
    print(enemy.health)
    mainGuy.attackEnemy(enemy)
