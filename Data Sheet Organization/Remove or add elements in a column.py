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
