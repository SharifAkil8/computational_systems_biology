import numpy as np
from scipy import stats

# Data
northern_wing_lengths = np.array([120, 113, 125, 118, 116, 114, 119])
southern_wing_lengths = np.array([116, 117, 121, 114, 116, 118, 123, 120])

# Sample sizes
n_northern = len(northern_wing_lengths)
n_southern = len(southern_wing_lengths)

# Calculate the means
mean_north = np.mean(northern_wing_lengths)
mean_south = np.mean(southern_wing_lengths)

# Sample variances
var_northern = np.var(northern_wing_lengths, ddof=1)
var_southern = np.var(southern_wing_lengths, ddof=1)

# Calculate pooled variance
s_pooled = ((n_northern - 1) * var_northern + (n_southern - 1) * var_southern) / (n_northern + n_southern - 2)

# Perform t-test
t_statistic, p_value = stats.ttest_ind(northern_wing_lengths, southern_wing_lengths, alternative='less')

print(f"Northern Mean: {mean_north}")
print(f"Southern Mean: {mean_south}")
print(f"Northern Variance: {var_northern}")
print(f"Southern Variance: {var_southern}")
print(f"Pooled Variance: {s_pooled}")
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")

U_statistic, p_value = stats.mannwhitneyu(northern_wing_lengths, southern_wing_lengths, alternative='two-sided')

# Combine both groups
combined = np.concatenate((northern_wing_lengths, southern_wing_lengths))

# Rank the combined data
ranks = stats.rankdata(combined)

# Assign ranks to each group
northern_ranks = ranks[:len(northern_wing_lengths)]
southern_ranks = ranks[len(northern_wing_lengths):]

# Sum the ranks for each group
R1 = np.sum(northern_ranks)
R2 = np.sum(southern_ranks)

print(f"Sum of Ranks for Northern (R1): {R1}")
print(f"Sum of Ranks for Southern (R2): {R2}")

print(f"U statistic: {U_statistic}")
print(f"P-value: {p_value}")