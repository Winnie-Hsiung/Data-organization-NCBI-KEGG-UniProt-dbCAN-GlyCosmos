
**A pile of codes**
** Please select what you need yourself**


----

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




----


# Convert tsv files to csv files

# folder name example:
# source_folder = "./data/tsv_files"
# output_folder = "./data/csv_files"

from pathlib import Path
import pandas as pd

def convert_tsv_to_csv(source_folder, output_folder):
    source = Path(source_folder).expanduser().resolve()
    output = Path(output_folder).expanduser().resolve()
    output.mkdir(parents=True, exist_ok=True)

    print(f"Looking for .tsv files in: {source}")
    tsv_files = list(source.glob("*.tsv"))

    if not tsv_files:
        print("No .tsv files found in the source folder.")
        return

    for tsv_file in tsv_files:
        try:
            df = pd.read_csv(tsv_file, sep="\t")
            csv_path = output / (tsv_file.stem + ".csv")
            df.to_csv(csv_path, index=False)
            print(f"✅ Converted: {tsv_file.name} → {csv_path.name}")
        except Exception as e:
            print(f"❌ Failed to convert {tsv_file.name}: {e}")

# Use raw strings to avoid issues with spaces
source_folder = r"/Users/Plantgarden_glycogene" # Replace with your folder path
output_folder = r"/Users/Plantgarden_glycogene_csv" # Replace with your folder path

convert_tsv_to_csv(source_folder, output_folder)


print("Files in source folder:")
for file in source.iterdir():
    print(f" - {file.name}")

