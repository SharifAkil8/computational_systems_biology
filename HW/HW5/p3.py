import pandas as pd
import scipy.stats as stats
import numpy as np

# Load Excel file
df = pd.read_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW5/ALL_AML_FS.xlsx', sheet_name='ALL_AML_FS')

initial_gene_count = df.iloc[:, 0].nunique()
print(f"Gene Count: {initial_gene_count}")

# Assuming numerical data starts from the 3rd column and considering the structure mentioned
# Extract paired samples
all_samples = df.iloc[:, 2:12].values  # First 10 after the first two columns are ALL
aml_samples = df.iloc[:, 12:22].values  # Next 10 are AML, matched with ALL samples

# Perform paired t-tests for each gene
paired_p_values = []
for i in range(len(df)):
    _, p_val = stats.ttest_rel(all_samples[i], aml_samples[i])
    paired_p_values.append(p_val)

# Add paired p-values to the DataFrame
df['paired_p_value'] = paired_p_values

# Count the number of significantly differentially expressed genes with the paired t-test
num_significant_genes_paired = df[df['paired_p_value'] < 0.05].shape[0]

print(f"Number of significantly differentially expressed genes with paired t-test: {num_significant_genes_paired}")

# Calculate the mean differences between matched ALL and AML samples for each gene
mean_differences = np.mean(aml_samples - all_samples, axis=1)

# Add the mean differences to the DataFrame
df['mean_difference'] = mean_differences

# Filter for significantly differentially expressed genes based on the paired t-test
significant_genes_paired = df[df['paired_p_value'] < 0.05]

# Determine how many of these genes are up-regulated in AML
# A positive mean difference indicates higher expression in AML
num_upregulated_in_aml_paired = significant_genes_paired[significant_genes_paired['mean_difference'] > 0].shape[0]

print(f"Number of genes up-regulated in AML identified with paired t-test: {num_upregulated_in_aml_paired}")
print(f"p-value: {p_val}")

# # Save the significantly differentially expressed genes to an Excel file
# significant_genes_paired.to_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW5/significant_genes_paired.xlsx', index=False)
# print("Significant genes saved to Excel.")

# Create a DataFrame from the p_values list
p_values_df = pd.DataFrame({'p_value': paired_p_values})

# Assuming your gene identifiers/descriptions are in the first column of `df`
p_values_df['Gene Identifier'] = df.iloc[:, 0].values

# # Save the p_values DataFrame to an Excel file
# p_values_df.to_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW5/p_values_p3.xlsx', index=False)
# print("p_values for the genes saved to Excel.")



# ///////////////////////////////////////////////////////////////////////////////////////////////////////
# ANOTHER WAY BELOW
# ///////////////////////////////////////////////////////////////////////////////////////////////////////



# import pandas as pd
# import scipy.stats as stats

# # Load Excel file
# df = pd.read_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW5/ALL_AML_FS.xlsx', sheet_name='ALL_AML_FS')

# initial_gene_count = df.iloc[:, 0].nunique()
# print(f"Gene Count: {initial_gene_count}")

# # Assuming df is your DataFrame with the first two columns being non-numeric (gene information) and the rest being your samples
# all_samples = df.iloc[:, 2:12]  # Adjust indices according to your DataFrame structure
# aml_samples = df.iloc[:, 12:22]

# # Calculate differences between matched pairs
# differences = aml_samples.values - all_samples.values

# # Perform a paired t-test on the differences for each gene
# p_values = [stats.ttest_1samp(differences[i, :], 0).pvalue for i in range(differences.shape[0])]

# # Add p-values to the DataFrame and filter based on significance
# df['paired_p_value'] = p_values
# significant_genes = df[df['paired_p_value'] < 0.05]

# # Determine the number of significantly differentially expressed genes and those up-regulated in AML
# num_significant_genes = significant_genes.shape[0]
# upregulated_in_aml = significant_genes[(aml_samples.mean(axis=1) - all_samples.mean(axis=1)) > 0].shape[0]

# print(f"Number of significantly differentially expressed genes (paired t-test): {num_significant_genes}")
# print(f"Number of genes up-regulated in AML (paired t-test): {upregulated_in_aml}")