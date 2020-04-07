def free_dice():
    import random
    dice=[1,2,3,4,5,6]
    y = int(input("How many Free dice would you like to roll: "))
    for i in range(y):
        print(random.choice(dice), end=" ")
    print(" ")