import numpy as np
import scipy.stats as stats

# Data
nitrogen_oxides = np.array([104, 116, 84, 77, 61, 84, 81, 72, 61, 97, 84])
hydrocarbons = np.array([108, 118, 89, 71, 66, 83, 88, 76, 68, 96, 81])

# Sample sizes
n_nitrogen_oxides = len(nitrogen_oxides)
n_hydrocarbons = len(hydrocarbons)

# Calculate the means
mean_nitrogen_oxides = np.mean(nitrogen_oxides)
mean_hydrocarbons = np.mean(hydrocarbons)

# Sample variances
var_nitrogen_oxides = np.var(nitrogen_oxides, ddof=1)
var_hydrocarbons = np.var(hydrocarbons, ddof=1)

# Calculate pooled variance
s_pooled = ((n_nitrogen_oxides - 1) * var_nitrogen_oxides + (n_hydrocarbons - 1) * var_hydrocarbons) / (n_nitrogen_oxides + n_hydrocarbons - 2)

# a. Paired T-Test
differences = nitrogen_oxides - hydrocarbons
t_statistic, p_value = stats.ttest_rel(nitrogen_oxides, hydrocarbons)

# b. 95% Confidence Interval for Mean Difference
mean_difference = np.mean(differences)
std_error = stats.sem(differences)
confidence_interval = stats.t.interval(0.95, len(differences)-1, loc=mean_difference, scale=std_error)

# c. Wilcoxon Signed-Rank Test
T_plus, T_minus = stats.wilcoxon(nitrogen_oxides, hydrocarbons)


print(f"Nitrogen Oxides Mean: {mean_nitrogen_oxides}")
print(f"Hydrocarbons Mean: {mean_hydrocarbons}")
print(f"Nitrogen Oxides Variance: {var_nitrogen_oxides}")
print(f"Hydrocarbons Variance: {var_hydrocarbons}")
print(f"Pooled Variance: {s_pooled}")
print(f"Paired T-Test t-statistic: {t_statistic}")
print(f"Paired T-Test p-value: {p_value}")
print(f"95% Confidence Interval for the mean difference: {confidence_interval}")
print(f"Wilcoxon T+ statistic: {T_plus}")
print(f"Wilcoxon T- statistic: {T_minus}")