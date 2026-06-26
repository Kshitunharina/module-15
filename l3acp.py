# Number of balls
red = 1
blue = 6
white = 3

# Total balls
total = red + blue + white

# Probability of second white given first white (with replacement)
probability = white / total

print("Total balls:", total)
print("White balls:", white)
print("Probability that the second ball is white given the first ball is white =", probability)