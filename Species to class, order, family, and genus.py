#Species to class and order

import pandas as pd
from ete3 import NCBITaxa

# Load NCBI taxonomy database
ncbi = NCBITaxa()  # You may need to update: ncbi.update_taxonomy_database()

# Read species names from CSV
df = pd.read_csv("Species names.csv")  # Replace with your file name/path
species_list = df["Org_name"].tolist()  # Replace 'species_name' with your column name

# Function to get class & order
def get_taxonomy(species_name):
    try:
        taxid = ncbi.get_name_translator([species_name])[species_name][0]
        lineage = ncbi.get_lineage(taxid)
        ranks = ncbi.get_rank(lineage)
        names = ncbi.get_taxid_translator(lineage)

        genus_name = next((names[t] for t in lineage if ranks[t] == "genus"), "Not found")        
        family_name = next((names[t] for t in lineage if ranks[t] == "family"), "Not found")
        class_name = next((names[t] for t in lineage if ranks[t] == "class"), "Not found")
        order_name = next((names[t] for t in lineage if ranks[t] == "order"), "Not found")

        return class_name, order_name, family_name, genus_name
    except:
        return "Not found", "Not found", "Not found", "Not found"

# Apply function to all species
df[[ "class", "order", "family", "genus"]] = df["Org_name"].apply(lambda x: pd.Series(get_taxonomy(x)))

# Save results to a new CSV
df.to_csv("Species_with_class_order.csv", index=False)

print("Classification completed. Results saved in 'species_with_class_order.csv'")
