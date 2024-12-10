from statsmodels.stats.multitest import multipletests
import pandas as pd

# Load the datasets from Excel files
df_q1 = pd.read_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW5/p_values_problem1.xlsx', sheet_name='Sheet1')
df_q2 = pd.read_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW5/p_values_p2.xlsx', sheet_name='Sheet1')

# Apply BH correction
df_q1['bh_corrected_p_value'] = multipletests(df_q1['p_value'], method='fdr_bh')[1]
df_q2['bh_corrected_p_value'] = multipletests(df_q2['p_value'], method='fdr_bh')[1]

# Identify significantly differentially expressed genes
significant_q1 = df_q1[df_q1['bh_corrected_p_value'] < 0.05]
significant_q2 = df_q2[df_q2['bh_corrected_p_value'] < 0.05]

# Determine up-regulated genes in AML
upregulated_q1 = significant_q1[significant_q1['mean_diff'] > 0]  # For Q1, use mean_difference
upregulated_q2 = significant_q2[significant_q2['median_diff'] > 0]  # For Q2, use median_difference

# Calculate the overlap
overlap_genes = set(significant_q1['Gene Identifier']).intersection(set(significant_q2['Gene Identifier']))
overlap_upregulated = overlap_genes.intersection(set(upregulated_q1['Gene Identifier']), set(upregulated_q2['Gene Identifier']))

# Results
print(f"Q1: {len(significant_q1)} significantly differentially expressed genes, {len(upregulated_q1)} up-regulated in AML")
print(f"Q2: {len(significant_q2)} significantly differentially expressed genes, {len(upregulated_q2)} up-regulated in AML")
print(f"Overlap between Q1 and Q2 gene sets: {len(overlap_genes)} genes")
print(f"Number of overlapping genes up-regulated in AML: {len(overlap_upregulated)}")