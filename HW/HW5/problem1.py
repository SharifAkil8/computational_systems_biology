import pandas as pd
import scipy.stats as stats
import numpy as np

# Load Excel file
df = pd.read_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW5/ALL_AML_FS.xlsx', sheet_name='ALL_AML_FS')

initial_gene_count = df.iloc[:, 0].nunique()
print(f"Gene Count: {initial_gene_count}")

# Isolate numerical data, first two columns are strings
numerical_data = df.iloc[:, 2:]

# Split the data into ALL and AML based on sample numbers
all_samples = numerical_data.iloc[:, :10]  # First 10 are ALL
aml_samples = numerical_data.iloc[:, -10:] # Last 10 are AML

# Initialize lists to store results
p_values = []
mean_diffs = []

# Perform t-tests for each gene
for index, row in numerical_data.iterrows():
    t_stat, p_val = stats.ttest_ind(all_samples.loc[index], aml_samples.loc[index], equal_var=True)
    p_values.append(p_val)
    mean_diffs.append(np.mean(aml_samples.loc[index]) - np.mean(all_samples.loc[index]))

# Add p-values and mean differences to the DataFrame
df['p_value'] = p_values
df['mean_diff'] = mean_diffs

# Filter to find significantly differentially expressed genes
significant_genes = df[df['p_value'] < 0.05]

# Number of significantly differentially expressed genes
num_significant_genes = significant_genes.shape[0]

# Genes up-regulated in AML (positive mean difference indicates higher expression in AML)
num_upregulated_in_aml = significant_genes[significant_genes['mean_diff'] > 0].shape[0]

print(f"Number of significantly differentially expressed genes: {num_significant_genes}")
print(f"Number of genes up-regulated in AML: {num_upregulated_in_aml}")
print(f"p-value: {p_val}")

# # Save the significantly differentially expressed genes to an Excel file
# significant_genes.to_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW5/significant_genes_p1.xlsx', index=False)
# print("Significant genes saved to Excel.")

# Create a DataFrame from the p_values list
p_values_df = pd.DataFrame({'p_value': p_values})

# Optionally, if you want to include gene identifiers or descriptions in the Excel file:
# Assuming your gene identifiers/descriptions are in the first column of `df`
p_values_df['Gene Identifier'] = df.iloc[:, 0].values

# # Save the p_values DataFrame to an Excel file
# p_values_df.to_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW5/p_values_problem1.xlsx', index=False)
# print("p_values for the genes saved to Excel.")