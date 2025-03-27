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






----

# Remove or add elements in a column

import pandas as pd

# Load the CSV file
input_file = "Species_with_class_order.csv"  # Ensure correct path
output_file = "Species_with_class_order_modified.csv"   # Ensure correct path

df = pd.read_csv(input_file)

# Remove '(' and ')' from column 'Glycan_structure', handling NaN values safely
df['Glycan_structure'] = df['Glycan_structure'].astype(str).str.replace(r'[()]', '', regex=True)

# Remove '-like' from column 'Glycan_structure', handling NaN values safely
df['Glycan_structure'] = df['Glycan_structure'].astype(str).str.replace(r'[-like]', '', regex=True)


# Save to a new CSV file
df.to_csv(output_file, index=False)

print(f"Modified file saved as {output_file}")


