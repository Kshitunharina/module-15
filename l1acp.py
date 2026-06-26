import random

# Roll the dice
dice = random.randint(1, 6)

# Display the dice number
print("Dice rolled:", dice)

# Probability of getting a 6
probability = 1 / 6
print("Probability of getting a 6 =", probability)

# Check if the dice shows 6
if dice == 6:
    print("The game can be started!")
else:
    print("Roll again")