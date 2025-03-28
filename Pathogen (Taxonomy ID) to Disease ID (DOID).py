# Pathogen/Taxonomy ID to Disease ID (DOID)
# Wait for the endpoint rework

import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON
import time

# SPARQL endpoint
sparql = SPARQLWrapper("https://www.pathophenodb.org/sparql")

# Input and output paths
input_csv = "/Users/organisms_with_taxids.csv"
output_csv = "/Users/disease_info_by_pathogen.csv"

# Load taxonomy IDs - when your pathogen id is taxnonomy id
df = pd.read_csv(input_csv)
tax_ids = df["Taxonomy_ID"].dropna().astype(str).unique()   # the column name is "Taxonomy_ID"

results_list = []

for tax_id in tax_ids:
    print(f"🔍 Querying tax_id: {tax_id}")
    
    query = f"""
    PREFIX SIO: <http://semanticscience.org/resource/SIO_>
    PREFIX RO: <http://purl.obolibrary.org/obo/RO_>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT DISTINCT ?Disease_ID ?Disease ?Pathogen_ID ?Pathogen ?evidence_Code    
    FROM <http://patho.phenomebrowser.net>
    WHERE 
    {{
        ?Disease_ID SIO:000255 ?o .  
        ?o RO:0002558 ?o1 .
        ?o RO:0002556  ?Pathogen_ID .
        ?Disease_ID rdfs:label ?Disease .
        ?Pathogen_ID rdfs:label ?Pathogen .
        ?o1 rdfs:label ?evidence_Code .

        FILTER(STR(?Pathogen_ID) = "http://purl.obolibrary.org/obo/NCBITaxon_{tax_id}")
    }}
    """

    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    try:
        response = sparql.query().convert()
        for result in response["results"]["bindings"]:
            pathogen_id_url = result["Pathogen_ID"]["value"]
            tax_id_extracted = pathogen_id_url.split("_")[-1] if "NCBITaxon_" in pathogen_id_url else None
            
            results_list.append({
                "tax_id": tax_id_extracted,
                "disease_name": result["Disease"]["value"],
                "doid": result["Disease_ID"]["value"].split("/")[-1],
                "pathogen_label": result["Pathogen"]["value"],
                "evidence_code": result["evidence_Code"]["value"]
            })
    except Exception as e:
        print(f"⚠️ Error for tax_id {tax_id}: {e}")

    time.sleep(1.4)  # Be gentle to the server

# Save results
results_df = pd.DataFrame(results_list)
results_df.to_csv(output_csv, index=False)
print(f"✅ Results saved to {output_csv}")
