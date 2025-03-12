#Use NCBI Gene ID to download KEGG ID, KEGG KO, and protein sequence


import requests
import pandas as pd
import time


def safe_request(url, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            if response.ok and response.text:
                return response.text.strip()
        except requests.RequestException as e:
            print(f"❌ Attempt {attempt+1}: Failed to fetch {url} - {e}")
        time.sleep(delay)
    return None

def get_kegg_id(ncbi_id):
    url = f"https://rest.kegg.jp/conv/genes/ncbi-geneid:{ncbi_id}"
    response_text = safe_request(url)
    return response_text.split("\t")[1].strip() if response_text else None


def get_kegg_info(kegg_id):
    kegg_data = {"KEGG_ID": kegg_id, "KEGG_KO": None, "UniProt_ID": None}

    # Get KEGG KO
    ko_url = f"https://rest.kegg.jp/link/ko/{kegg_id}"
    response_text = safe_request(ko_url)
    if response_text:
        kegg_data["KEGG_KO"] = response_text.split("\t")[1].strip()

    return kegg_data

def get_uniprot_id(ncbi_ids):
    url = "https://rest.uniprot.org/idmapping/run"
    data = {"from": "GeneID", "to": "UniProtKB", "ids": ",".join(ncbi_ids)}
    response = requests.post(url, data=data)
    if response.ok:
        return response.json()
    return {}


def get_protein_sequence(kegg_id):
    url = f"https://rest.kegg.jp/get/{kegg_id}/aaseq"
    response_text = safe_request(url)
    return response_text if response_text else ""

def write_faa(sequences, filename):
    with open(filename, "w") as f:
        for kegg_id, seq in sequences.items():
            if seq:
                f.write(f">{kegg_id}\n{seq}\n")




def main(input_csv, output_csv, faa_file):
    df = pd.read_csv(input_csv)
    ncbi_gene_ids = df['NCBI_Gene_ID'].dropna().astype(str).tolist()
    
    sequences = {}
    results = []
    
    uniprot_mapping = get_uniprot_id(ncbi_gene_ids)
    
    for gene_id in ncbi_gene_ids:
        print(f"🟢 Processing Gene ID: {gene_id}")
        kegg_id = get_kegg_id(gene_id)
        kegg_info = get_kegg_info(kegg_id) if kegg_id else {"KEGG_ID": None, "KEGG_KO": None}
        uniprot_id = uniprot_mapping.get(gene_id, None)
        protein_seq = get_protein_sequence(kegg_id) if kegg_id else None
    
        if kegg_id and protein_seq:
            sequences[kegg_id] = protein_seq
        else:
            print(f"⚠️ Warning: No KEGG ID or protein sequence found for Gene ID {gene_id}")
    
        results.append({
            "NCBI_Gene_ID": gene_id,
            **kegg_info,
            "UniProt_ID": uniprot_id,
            "Protein_Sequence": protein_seq if protein_seq else "Not found"
        })
        time.sleep(4)
    
 
    
    df_results = pd.DataFrame(results)
    df_results.to_csv(output_csv, index=False)
    print(f"📝 Results saved to {output_csv}")




if __name__ == "__main__":
    input_csv = "input.csv"
    output_csv = "output.csv"
    faa_file = "protein_sequences.faa"
    main(input_csv, output_csv, faa_file)
