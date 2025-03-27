# Data sorting - merge columns into one csv file

import pandas as pd

# Load the CSV files - file path
b_df = pd.read_csv('B.csv', usecols=['GeneID', 'A', 'UniProt_ID', 'Entry Name', 'Protein names', 'Gene Names', 'Organism', 'Length', 'Organism (ID)'])  # Load only necessary columns
c_df = pd.read_csv('C.csv')  # Load the entire C file

# Merge A... columns from B into C based on 'GeneID' column
merged_df = c_df.merge(b_df, on='GeneID', how='left')  # Use left join to preserve all rows from C


# Save the result
merged_df.to_csv('merged.csv', index=False) #Replace with your file path

print("Merge complete. Output saved to merged.csv")


