from scipy.stats import binom

# Total number of days
n = 30

# Expected rainy days = 10
p = 10 / 30

# Probability of 12 or more rainy days
prob1 = 1 - binom.cdf(11, n, p)

# Probability of 12 to 18 rainy days
prob2 = binom.cdf(18, n, p) - binom.cdf(11, n, p)

# Display the answers
print("Probability of 12 or more rainy days:", round(prob1, 4))
print("Probability of 12 to 18 rainy days:", round(prob2, 4))