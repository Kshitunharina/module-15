from math import comb

# Total coin flips
n = 10

# Chance of getting a head
p = 0.5

# Probability of getting 2, 3, or 4 heads
probability = 0

for heads in range(2, 5):
    probability = probability + comb(n, heads) * (p ** heads) * ((1 - p) ** (n - heads))

print("Probability =", probability)