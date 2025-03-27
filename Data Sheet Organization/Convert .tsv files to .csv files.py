# Convert .tsv files to .csv files


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
