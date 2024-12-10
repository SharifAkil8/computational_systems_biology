import pandas as pd

# Load the datasets from Excel files
df_q1 = pd.read_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW5/significant_genes_p1.xlsx', sheet_name='Sheet1')
df_q2 = pd.read_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW5/significant_genes_p2.xlsx', sheet_name='Sheet1')
df_q3 = pd.read_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW5/significant_genes_paired.xlsx', sheet_name='Sheet1')
df_q4 = pd.read_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW5/significant_genes_wilcoxon.xlsx', sheet_name='Sheet1')

# Assuming 'Gene Accession Number' is the column with gene identifiers
genes_q1 = set(df_q1['Gene Accession Number'])
genes_q2 = set(df_q2['Gene Accession Number'])
genes_q3 = set(df_q3['Gene Accession Number'])
genes_q4 = set(df_q4['Gene Accession Number'])

# Calculate overlaps
overlap_q1_q2 = genes_q1.intersection(genes_q2)
overlap_q1_q3 = genes_q1.intersection(genes_q3)
overlap_q2_q4 = genes_q2.intersection(genes_q4)
overlap_q3_q4 = genes_q3.intersection(genes_q4)

# Display the counts
print(f"Overlap between Q1 and Q2: {len(overlap_q1_q2)} genes")
print(f"Overlap between Q1 and Q3: {len(overlap_q1_q3)} genes")
print(f"Overlap between Q2 and Q4: {len(overlap_q2_q4)} genes")
print(f"Overlap between Q3 and Q4: {len(overlap_q3_q4)} genes")