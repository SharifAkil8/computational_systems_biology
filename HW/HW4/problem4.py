import statistics
import numpy as np
from scipy import stats

# Data
male_cholesterol = np.array([220.1, 218.6, 229.6, 228.8, 222.0, 224.1, 226.5])
female_cholesterol = np.array([223.4, 221.5, 230.2, 224.3, 223.8, 230.8])

# Sample sizes
n_male = len(male_cholesterol)
n_female = len(female_cholesterol)

# Calculate the means
mean_male = np.mean(male_cholesterol)
mean_female = np.mean(female_cholesterol)

# Calculate the standard deviations
male_std_dev = statistics.stdev(male_cholesterol)
female_std_dev = statistics.stdev(female_cholesterol)

# Sample variances
var_male = np.var(male_cholesterol, ddof=1)
var_female = np.var(female_cholesterol, ddof=1)

# Calculate pooled standard deviation
s_pooled = np.sqrt(((n_male - 1) * var_male + (n_female - 1) * var_female) / (n_male + n_female - 2))

# Perform independent two-sample t-test
t_statistic, p_value = stats.ttest_ind(male_cholesterol, female_cholesterol, equal_var=True)

print(f"Male Mean: {mean_male}")
print(f"Female Mean: {mean_female}")
print(f"Male Standard Deviation: {male_std_dev}")
print(f"Female Standard Deviation: {female_std_dev}")
print(f"Male Variance: {var_male}")
print(f"Female Variance: {var_female}")
print(f"Pooled standard deviation (s_pooled): {s_pooled}")
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")