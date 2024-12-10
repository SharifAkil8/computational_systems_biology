from scipy import stats
import numpy as np

# Data
diploid = [248, 236, 269, 254, 249, 251, 260, 245, 239, 255]
triploid = [380, 391, 377, 392, 398, 374]

n1 = len(diploid)
n2 = len(triploid)

# Perform the Mann-Whitney U test
p_value = stats.mannwhitneyu(diploid, triploid, alternative='two-sided')

# Combine both groups
combined = np.concatenate((diploid, triploid))

# Rank the combined data
ranks = stats.rankdata(combined)

# Assign ranks to each group
diploid_ranks = ranks[:len(diploid)]
triploid_ranks = ranks[len(diploid):]

# Sum the ranks for each group
R1 = np.sum(diploid_ranks)
R2 = np.sum(triploid_ranks)

print(f"Sum of Ranks for Northern (R1): {R1}")
print(f"Sum of Ranks for Southern (R2): {R2}")

# Calculate U
U = (n1 * n2) + ((n1 * (n1 + 1)) / 2) - R1

# Calculate U’
U_prime = (n1 * n2) + ((n2 * (n2 + 1)) / 2) - R2

print(f"U statistic: {U}")
print(f"U' statistic: {U_prime}")
print(f"P-value: {p_value}")