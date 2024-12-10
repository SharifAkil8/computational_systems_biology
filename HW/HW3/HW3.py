import pandas as pd
import numpy as np
import openpyxl
from scipy import stats

# Load Excel file
df = pd.read_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW3/ALL_AML_Test_HW3.xlsx', sheet_name='ALL_AML_Test')  # Adjust the sheet name as necessary

initial_gene_count = df.iloc[:, 1].nunique()  # Second column has unique gene identifiers
print(f"Initial number of genes: {initial_gene_count}")

# Find columns that are numeric
numeric_cols = df.select_dtypes(include=['number']).columns

# Find columns that are strings
string_cols = df.select_dtypes(include=['object', 'string']).columns

# Find genes with negative values
genes_with_negative_values = (df[numeric_cols] < 0).any(axis=1)

# Filter out genes with any negative values
filtered_df = df[~genes_with_negative_values]

# Count the remaining genes
remaining_genes_count = filtered_df.iloc[:, 1].nunique()
print(f"Number of genes after removing those with negative values: {remaining_genes_count}")

# Calculate mean signal value for each sample (column)
mean_signal_values = filtered_df[numeric_cols].mean()

# Print mean signal values
print(f"Mean signal values for each sample: {mean_signal_values}")

# Calculate the 2% trimmed mean for each numeric column (sample)
trimmed_means = {}
for col in numeric_cols:
    trimmed_mean = stats.trim_mean(filtered_df[col], proportiontocut=0.02)  # Trimming 2% from both ends
    trimmed_means[col] = trimmed_mean

# Convert the dictionary to a pandas Series for nicer display
trimmed_means_series = pd.Series(trimmed_means, name="2% Trimmed Mean")

# Print the 2% trimmed mean values
print(f"2% Trimmed mean signal values for each sample: {trimmed_means_series}")

# Define target intensity
target_intensity = 1500

# Calculate scaling factor for each sample
scaling_factors = target_intensity / mean_signal_values

# Print scaling factors
print(f"Scaling factors for each sample: {scaling_factors}")

# Apply scaling factors to the numeric columns
for col in numeric_cols:
    filtered_df[col] = filtered_df[col] * scaling_factors[col]

# Identify genes to remove based on 'Absent' calls
# The 'Absent'/'Present' calls are in the string columns
absent_count = filtered_df[string_cols].apply(lambda x: (x == 'A').sum(), axis=1)

# Filter out genes with 15 or more 'Absent' calls
genes_to_keep = absent_count < 15
scaled_and_filtered_df = filtered_df[genes_to_keep]

# Count the remaining genes
remaining_genes_count_after_absent_filter = scaled_and_filtered_df.iloc[:, 1].nunique()
print(f"Number of genes after removing those with negative values and 'Absent' in 15 or more samples: {remaining_genes_count_after_absent_filter}")

# numeric_cols contains the correct order corresponding to sample numbers
# the first column in numeric_cols is the gene identifier column which should be skipped

# Extract columns for ALL and AML samples based on their sample numbers
# For sample numbers 1-10 (ALL) and 29-38 (AML)
all_samples = numeric_cols[0:10]
aml_samples = numeric_cols[10:20]

# Calculate average signal values for AML and ALL samples for each gene
A_ALL = scaled_and_filtered_df[all_samples].mean(axis=1)
A_AML = scaled_and_filtered_df[aml_samples].mean(axis=1)

# Calculate fold change for each gene
fold_change = A_AML / A_ALL

# Filter genes with fold change > 2
upregulated_genes = fold_change[fold_change > 2]

# Print the number of upregulated genes
print(f"Number of upregulated genes in AML with fold change > 2: {len(upregulated_genes)}")

# Filter genes with fold change < 0.5 for downregulated genes
downregulated_genes = fold_change[fold_change < 0.5]

# Print the number of downregulated genes
print(f"Number of downregulated genes in AML with fold change < 0.5: {len(downregulated_genes)}")