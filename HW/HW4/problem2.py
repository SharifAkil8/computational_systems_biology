import statistics
from scipy import stats
import math

# Sample data
data = [26, 24, 29, 33, 25, 26, 23, 30, 31, 30, 28, 27, 29, 26, 28]

# Calculate the sample mean and standard deviation
mean = statistics.mean(data)
std_dev = statistics.stdev(data)

# Sample size
n = len(data)

# Degrees of freedom
df = n - 1

# Find the t-value for a 95% confidence interval
# We're doing a two-tailed test, so we use 0.025 (2.5% in each tail)
t_value = stats.t.ppf(1 - 0.025, df)

# Calculate the margin of error
standard_error = std_dev / math.sqrt(n)
margin_of_error = t_value * standard_error

# Calculate the confidence interval
confidence_interval = (mean - margin_of_error, mean + margin_of_error)

print(f"Mean: {mean}")
print(f"Standard Deviation: {std_dev}")
print(f"Degrees of Freedom: {df}")
print(f"T-value: {t_value}")
print(f"Margin of Error: {margin_of_error}")
print(f"95% Confidence Interval: {confidence_interval}")