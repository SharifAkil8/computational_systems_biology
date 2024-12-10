import numpy as np
from scipy import stats
from scipy.stats import t

# Sample data
calcium_concentrations = np.array([28, 27, 29, 29, 30, 30, 31, 30, 33, 27, 30, 32, 31])

# Mean of the sample
mean_sample = np.mean(calcium_concentrations)

# Standard deviation of the sample
std_sample = np.std(calcium_concentrations, ddof=1)

# Population mean
mu = 32

# Sample size
n = len(calcium_concentrations)

# Calculate t-statistic
t_statistic = (mean_sample - mu) / (std_sample / np.sqrt(n))

# Degrees of freedom
df = n - 1

# Significance level for a one-tailed test
alpha = 0.05

# Calculate the critical t-value
critical_t_value = t.ppf(1 - alpha, df)

# Calculate p-value for one-tailed test
p_value = stats.t.cdf(t_statistic, df)

print(f"Mean of the sample: {mean_sample}")
print(f"Standard deviation of the sample: {std_sample}")
print(f"T-statistic: {t_statistic}")
print(f"Critical t-value for a one-tailed test with df=12 at alpha=0.05: {critical_t_value}")
print(f"P-value: {p_value}")