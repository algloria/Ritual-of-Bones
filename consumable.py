import random
class Consumable:
    def __init__(self, name, damage, spirit, frolls,cm):
        self.name = name
        self.damage = damage
        self.spirit = spirit
        self.frolls = frolls
        self.cm = cm


consumable_list=[]
consumable_list.append(Consumable("Beef Jerky", 0, 20, 0, 15))
consumable_list.append(Consumable("Campfire Coffee", 0, 15, 0, 10))
consumable_list.append(Consumable("Campfire Tea", 0, 10, 0, 8))
consumable_list.append(Consumable("Roasted Bear Meat", 0, 30, 0, 25 ))
consumable_list.append(Consumable("Hemp Joint", 0, 15, 0, 10))
consumable_list.append(Consumable("Carved Wooden Spoon", 0, 10, 0, 8))
consumable_list.append(Consumable("Pot of Vegetable Soup", 0, 40, 0, 35))

weapon_list=[]
weapon_list.append(Consumable("Bow and Arrow", 20, 0, 0, 15))
weapon_list.append(Consumable("Iron Spear", 30, 0, 0, 25))
weapon_list.append(Consumable("Iron Battle Axe", 40, 0, 0, 35))
weapon_list.append(Consumable("Throwing Axe", 15, 0, 0, 10))
weapon_list.append(Consumable("Stone Knife",15, 0, 0, 10))
weapon_list.append(Consumable("Stone Hatchet", 20, 0, 0, 15))
weapon_list.append(Consumable("Cursed Sacrifical Dagger", 50, 0, 0, 45))

treasure_list=[]
treasure_list.append(Consumable("Golden Carrot", 0, 0, 2, 0))
treasure_list.append(Consumable("Iron Chest", 0, 0, 5, 0))
treasure_list.append(Consumable("Ancient Golden Chest", 0, 0, 8, 0))
treasure_list.append(Consumable("Wooden Chest", 0, 0, 3, 0))
treasure_list.append(Consumable("8 Leaf Clover", 0, 0, 4, 0))
treasure_list.append(Consumable("Sparkling Rock",0 ,0, 2, 0))




















# consumable_list.append(Consumable("Deadfall Trap"))
# consumable_list.append(Consumable("Rain Dance"))
# consumable_list.append(Consumable("Pitfall Trap"))
# consumable_list.append(Consumable("Loop Snare"))
# consumable_list.append(Consumable("Animal Sacrifice"))
# consumable_list.append(Consumable("Shaman Ritual"))


