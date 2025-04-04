
# Combine all .fa files in a folder

import glob

# Get a list of all .fa or .fasta files in the folder
fasta_files = glob.glob("/Users/folder/*.fa")  # or use "*.fasta", "*.faa"

# Output file name
output_file = "/Users/folder/combined_sequences.fa" # or use "*.fasta", "*.faa"

# Combine all files
with open(output_file, "w") as outfile:
    for fname in fasta_files:
        with open(fname, "r") as infile:
            contents = infile.read()
            outfile.write(contents)
            if not contents.endswith("\n"):
                outfile.write("\n")  # Ensure newline between sequences

print("Saved merged .fa file") # or .faa
