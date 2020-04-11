import random

dice_list=["Blank","Event","Animal Encounter","Consumable","Weapon"]
#dicex=random.choice(dice_list)
#dicey=random.choice(dice_list)
def roll():
        roll_1=random.choice(dice_list)
        roll_2=random.choice(dice_list)
        print(roll_1, roll_2)
        return roll_1, roll_2


      