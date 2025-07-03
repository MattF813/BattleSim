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

    def attackEnemy(self, enemy):
        super().attackEnemy(enemy)
        if enemy.killed:
            self.magic = self.magicMax
            self.health = self.healthMax
            self.lvl += 1
            print("Congratulations! " + self.name + " has reached level " + str(self.lvl) + ". Health and Mana have been restored!")


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
