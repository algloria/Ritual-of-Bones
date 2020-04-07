import freedice
import Dice
import animalcards
import random

damage=[1,2,3,4,5,6]

print("Welcome to Ritual of Bones\n")
print("A card game about surviving in the wilderness and pleasing the spirts of otherly realms")
print("Lets begin by first picking your class")

Spirit=20
choice=input("Shaman, Forest Hunter, Blacksmith, Survivalist ")
if choice=="Shaman":
    print("You have chosen the path of a shaman, you have great powers in pleasing the spirits. if the spirits are pleased enough, you may reach enlightnment and survive")
elif choice=="Forest Hunter":
    print("You have chosen the path of the Forest Hunter, Your goal is to hunt wild game to earn free rolls at the cost of your spirit. Free rolls are a powerful tool in this vast wilderness")
elif choice=="Blacksmith":
    print("As a black smith, you have the power to forge powerful weapons with free rolls. Use these weapons to fight off creatures of the wild and survive.")
elif choice=="Survivalist":
    print("As a survivalist, you have the ability to adapt to any situation. Good or bad, you are prepared for what the wilderness has to offer to you.")


while True:
    choice=input("Roll the Bones? Y/N")
    if choice== "Y"or choice =="y":
        roll_1, roll_2 = Dice.roll()
        if roll_1 =="Animal Encounter" or roll_2=="Animal Encounter":
            print("You spot an animal....")
            animal = random.choice(animalcards.animal_list)
            print(f"its a {animal.name}!")
            while animal.health > 0:
                attack=random.choice(damage)
                choice=input("Attack or Run Away? ")
                if choice== "Attack"or choice=="attack":
                    animal.health-=attack
                    print(f"You attack the {animal.name} for {attack} damage!")
                    print(f"The {animal.name}'s health is now {animal.health}")
                    if animal.health > 0:
                        animalattack=random.choice(animal.power)
                        Spirit-=animalattack
                        print(f"The {animal.name} has attacked you for {animalattack}")
                        print(f"Your health is now {Spirit}.")
                    if Spirit <= 0:
                        print("Game Over")
                        input()
                        exit()

                        
            
            
            




    elif choice=="N"or choice=="n":
        choice=input("Would you like to roll a free die? Y/N? ")
        if choice=="N"or choice=="n":
            print("You must either Roll the Bones or free dice")
        elif choice=="Y"or choice=="y":
            freedice.free_dice()
    