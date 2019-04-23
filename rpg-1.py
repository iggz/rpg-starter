"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""


class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            return True
        else:
            print("%s is dead." % (self.name))

    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

    def attack(self, enemy):
        enemy.health -= self.power
        print("%s did %d damage to the %s." % (self.name, self.power, enemy.name))



class Hero(Character):
    pass


class Goblin(Character):
    pass

class Zombie(Character):
    pass


hiro = Hero("Hero", 10, 5)
goblin = Goblin("Goblin", 6, 2)
zombie = Zombie("Zombie", 100, 12)

def main():
    
    while goblin.alive() and hiro.alive():
        #print("You have %d health and %d power." % (hiro.health, hiro.power))
        #print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
        hiro.print_status()
        goblin.print_status()
        zombie.print_status()

        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("4. fight zombie")
        print("> ",)
        user_input = input()
        if user_input == "1":
            hiro.attack(goblin)
            if goblin.health > 0:
                goblin.attack(hiro)
            # Hero attacks goblin
            # goblin.health -= hiro.power
            # print("You do %d damage to the goblin." % hiro.power)
            #if goblin.health <= 0:
            #    print("The goblin is dead.")
                
        elif user_input == "2":
            if goblin.health > 0:
                goblin.attack(hiro)
            
        
        elif user_input == "3":
            print("Goodbye.")
            break
        elif user_input == "4":
            zombie.attack(hiro)
        else:
            print("Invalid input %r" % user_input)

        #if goblin.health > 0:
            # Goblin attacks hero
            #hiro.health -= goblin.power
            #goblin.attack(hiro)
            #if hiro.health <= 0:
            #    print("You are dead.")
            #if goblin.health < 3:
            #    zombie.attack(hiro)

main()
