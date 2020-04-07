import random
class Animals:
    def __init__(self, name, health, power, paces, frolls):
        self.name = name
        self.health = health
        self.power = power
        self.paces = paces
        self.frolls = frolls

animal_list=[]
animal_list.append(Animals("Grizzly Bear",20, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 0, 10))
animal_list.append(Animals("Squirrel", 4, 0, 1, 2))
animal_list.append(Animals("Goldeneye", 4, 0, 1, 2))
animal_list.append(Animals("Jack Rabbit", 4, 0, 1, 2))
animal_list.append(Animals("Badger", 5, 0, 2, 2))
animal_list.append(Animals("Black Grouse", 5, 0, 2, 3))
animal_list.append(Animals("Capercaillie", 5, 0, 2, 3))
animal_list.append(Animals("Beaver", 6, 0, 2, 4))
animal_list.append(Animals("Elusive Fox",8 ,0, 3, 5))
animal_list.append(Animals("Wild Boar",12, [1,2,3,4,5,6,7,8], 0, 5))
animal_list.append(Animals("Black Bear", 14, [1,2,3,4,5,6,7,8,9,10,11,12], 0, 6))
animal_list.append(Animals("Panther", 12, [1,2,3,4,5,6,7,8,9,10,11,12], 0, 6))
animal_list.append(Animals("Forest Wolf", 12, [1,2,3,4,5,6,7,8,9,10,11,12], 0, 6))
animal_list.append(Animals("Bobcat", 10, [1,2,3,4,5,6,7,8], 0, 5))
animal_list.append(Animals("Large Elk", 18, 0, 4, 10))
animal_list.append(Animals("Hyena", 10, [1,2,3,4,5,6,7,8,9,10,11,12], 0, 5))
animal_list.append(Animals("Rattle Snake", 8, [1,2,3,4,5,6,7,8,9,10,11,12], 0, 5))
animal_list.append(Animals("Horned Owl", 8, [1,2,3,4,5,6,7,8,9,10,11,12], 0, 5))
animal_list.append(Animals("Eagle", 8, [1,2,3,4,5,6,7,8,9,10,11,12], 0, 5))
animal_list.append(Animals("Reindeer", 15, 0, 2, 8))
animal_list.append(Animals("Titan Boa", 15, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 0, 8))
animal_list.append(Animals("Black Bison",18, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 0, 10))
animal_list.append(Animals("Crocodile", 20, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 0, 10))
animal_list.append(Animals("Tribesman", 10, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 0, 6))
animal_list.append(Animals("Tribeswoman", 10, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 0, 6))
animal_list.append(Animals("God Bear", 30, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40], 0, 15))

ranimal=random.choice(animal_list)
