import freedice
import Dice
import animalcards
import consumable
import random

damage=[1,2,3,4,5,6]
itemdamage=[]
inventory=[]
freerolls=int()
material=[]

consumable.weapon_list
consumable.consumable_list

print("Welcome to Ritual of Bones\n")
print("A card game about surviving in the wilderness and pleasing the spirts of otherly realms")
print("Lets begin by first picking your class")

Spirit=30
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
    choice=input("Roll the Bones? Y/N ")
    if choice== "Y"or choice =="y":
        roll_1, roll_2 = Dice.roll()

        if roll_1 =="Animal Encounter" or roll_2=="Animal Encounter":
            print("You spot an animal....")
            animal = random.choice(animalcards.animal_list)
            print(f"its a {animal.name}!")
            while animal.health > 0:
                attack=random.choice(damage)
                choice=input("Attack or Run Away?")
                if choice== "Attack"or choice=="attack":
                    animal.health-=attack
                    animal.paces-= 1
                    print(f"You attack the {animal.name} for {attack} damage!\n")
                    print(f"The {animal.name}'s health is now {animal.health}\n")
                    if animal.health > 0:
                        animalattack=random.choice(animal.power)
                        Spirit-=animalattack
                        print(f"The {animal.name} has attacked you for {animalattack}\n")
                        print(f"Your health is now {Spirit}.")
        
                    if animal.health <=0:
                       print(f"the {animal.name} has been slayed!\n")
                       print(f"You have recived {animal.frolls} crafting material.")
                       material.append(animal.frolls)
                       damage=[1,2,3,4,5,6]
                       break
                    if animal.paces == 0:
                       print(f"the {animal.name} ran away!!...\n")
                       break
                    if Spirit <= 0:
                        print("Game Over")
                        input()
                        exit()
                elif choice == "Run away" or choice == "run away" or choice=="run":
                    print(f"You manage to sneak past the {animal.name}\n")
                    break

        if roll_1 == "Consumable" or roll_2 == "Consumable":
            item=random.choice(consumable.consumable_list)
            treasure=random.choice(consumable.treasure_list)
            choice=input(f"Would you like to go adventuring or rest? Venture/Rest. ")
            if choice=="venture" or choice== "Venture":
                Spirit-=5
                inventory.append(treasure)
                print(f"While you venture throughout the wilderness you stumble upon {treasure.name}! you store your findings in your inventory.")
                print(f"You also tire yourself out and lose 5 spirit. Your total spirit is now {Spirit}")
            elif choice=="Rest" or choice=="rest":
                print("You have decided to take this time sit down and rest...")



    elif choice=="N"or choice=="n":
        choice=input("Would you like to roll a free die? Y/N? ")
        if choice=="N"or choice=="n":
            print("You must either Roll the Bones or free dice")
        elif choice=="Y"or choice=="y":
            freedice.free_dice()
    
    elif choice =="inventory" or choice=="Inventory":
        for item in inventory:
            print(item.name)

    elif choice =="crafting" or choice=="materials":
            print(sum(material))

    
    elif choice =="health" or choice== "health":
        print(Spirit)

    elif choice =="Crafting Menu" or choice == "crafting menu":
        for consumable in consumable.consumable_list:
            print(f"{consumable.name} = {consumable.cm} crafting mat.")

    elif choice =="Weapon Menu" or choice == "weapon menu":
        for weapon in consumable.weapon_list:
            print(f"{weapon.name} = {weapon.cm} crafting mat.")

    elif choice =="craft" or choice =="craft":
        choice=input("Which weapon would you like to craft? ")
        for weapon in consumable.weapon_list:
            if choice == (f"{weapon.name}"):
                x = sum(material)-weapon.cm
                if x >= 0:
                    inventory.append(weapon)
                    print(f"You have crafted a {weapon.name}")
                if x <=0:
                    print("You do not have enough materials to make that item")
            

        
            
    elif choice == "equip item" or choice=="use item":
        for item in inventory:
            print(f"{inventory.index(item)}: {item.name}")
        item_choice = int(input("Which item would you like to use? ")) #removed int
        itemchoice=inventory.pop(item_choice) #changed inventory.pop to inventory.remove
        print(f"you have equiped/used {itemchoice.name}.")
        itemdamage.append(itemchoice.damage)
        weapondamage=list(range(1, itemchoice.damage))
        damage.extend(weapondamage)
        
        
        