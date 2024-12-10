import pandas as pd
import numpy as np
import scipy.stats as stats

# Load Excel file
df = pd.read_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW5/ALL_AML_FS.xlsx', sheet_name='ALL_AML_FS')

initial_gene_count = df.iloc[:, 0].nunique()
print(f"Gene Count: {initial_gene_count}")

# Isolate numerical data, skipping the first two columns which are strings
numerical_data = df.iloc[:, 2:]

# Extract paired samples
all_samples = numerical_data.iloc[:, :10].values  # Assuming the first 10 are ALL samples
aml_samples = numerical_data.iloc[:, -10:].values # Assuming the last 10 are AML samples, matched

# Initialize lists to store results
wilcoxon_p_values = []
mean_differences = []

# Perform Wilcoxon signed-rank tests for each gene
for i in range(len(df)):
    # Using continuity correction and exact method for p-value calculation
    stat, p_val = stats.wilcoxon(all_samples[i], aml_samples[i], zero_method='wilcox', correction=False, alternative='two-sided', mode='exact')
    wilcoxon_p_values.append(p_val)
    mean_differences.append(np.median(aml_samples[i]) - np.median(all_samples[i]))

# Add Wilcoxon p-values and median differences to the DataFrame
df['wilcoxon_p_value'] = wilcoxon_p_values
df['median_difference'] = mean_differences

# Filter to find significantly differentially expressed genes
significant_genes_wilcoxon = df[df['wilcoxon_p_value'] < 0.05]

# Number of significantly differentially expressed genes with the Wilcoxon test
num_significant_genes_wilcoxon = significant_genes_wilcoxon.shape[0]

# Genes up-regulated in AML (positive median difference indicates higher expression in AML)
num_upregulated_in_aml_wilcoxon = significant_genes_wilcoxon[significant_genes_wilcoxon['median_difference'] > 0].shape[0]

print(f"Number of significantly differentially expressed genes with Wilcoxon test: {num_significant_genes_wilcoxon}")
print(f"Number of genes up-regulated in AML identified with Wilcoxon test: {num_upregulated_in_aml_wilcoxon}")
print(f"p-value: {p_val}")

# # Save the significantly differentially expressed genes to an Excel file
# significant_genes_wilcoxon.to_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW5/significant_genes_wilcoxon.xlsx', index=False)
# print("Significant genes saved to Excel.")

# Create a DataFrame from the p_values list
p_values_df = pd.DataFrame({'p_value': wilcoxon_p_values})

# Assuming your gene identifiers/descriptions are in the first column of `df`
p_values_df['Gene Identifier'] = df.iloc[:, 0].values

# # Save the p_values DataFrame to an Excel file
# p_values_df.to_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW5/p_values_p4.xlsx', index=False)
# print("p_values for the genes saved to Excel.")