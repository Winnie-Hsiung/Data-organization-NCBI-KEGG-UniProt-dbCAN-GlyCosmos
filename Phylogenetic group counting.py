# If you want to know organisms' taxanomy and phylogenetic relationships, but Entrez gives you wrong classifications
# Use this code to categorize your data
# Modify the family names to fit your data

import pandas as pd
import os

def classify_cotyledon_type(family_name):
    """
    Classify plant families as monocotyledon or dicotyledon.
    
    Args:
        family_name (str): Name of the plant family
        
    Returns:
        str: 'Monocotyledon', 'Dicotyledon', or 'Unknown/Not a plant family'
    """
    
    # Handle NaN or empty values
    if pd.isna(family_name) or family_name == '':
        return 'Unknown/Not a plant family'
    
    # Convert to lowercase for case-insensitive matching
    family = str(family_name).lower().strip()

    
    # Common monocotyledon families
    monocot_families = {
        'poaceae', 'gramineae',  # Grass family
        'orchidaceae',           # Orchid family
        'liliaceae',            # Lily family
        'arecaceae', 'palmae',  # Palm family
        'amaryllidaceae',       # Amaryllis family
        'iridaceae',            # Iris family
        'bromeliaceae',         # Bromeliad family
        'musaceae',             # Banana family
        'zingiberaceae',        # Ginger family
        'araceae',              # Arum family
        'commelinaceae',        # Spiderwort family
        'cyperaceae',           # Sedge family
        'asparagaceae',         # Asparagus family
        'alliaceae',            # Onion family
        'hydrocharitaceae',     # Tape-grass family
        'alismataceae',         # Water-plantain family
        'juncaceae',            # Rush family
        'typhaceae',            # Cattail family
        'pandanaceae',          # Screw-pine family
        'dioscoreaceae',        # Yam family
        'zosteraceae',
        'cannaceae',
        'acoraceae',
        'hyacinthaceae',
        
    }
    
    # Common dicotyledon families
    dicot_families = {
        'rosaceae',             # Rose family
        'fabaceae', 'leguminosae',  # Pea/Bean family
        'asteraceae', 'compositae',  # Sunflower/Daisy family
        'brassicaceae', 'cruciferae',  # Mustard family
        'solanaceae',           # Nightshade family
        'lamiaceae', 'labiatae',  # Mint family
        'apiaceae', 'umbelliferae',  # Carrot family
        'malvaceae',            # Mallow family
        'euphorbiaceae',        # Spurge family
        'rubiaceae',            # Coffee family
        'scrophulariaceae',     # Figwort family
        'ranunculaceae',        # Buttercup family
        'caryophyllaceae',      # Pink family
        'polygonaceae',         # Buckwheat family
        'convolvulaceae',       # Morning glory family
        'boraginaceae',         # Borage family
        'plantaginaceae',       # Plantain family
        'onagraceae',           # Evening primrose family
        'geraniaceae',          # Geranium family
        'violaceae',            # Violet family
        'cucurbitaceae',        # Gourd family
        'amaranthaceae',        # Amaranth family
        'chenopodiaceae',       # Goosefoot family
        'papaveraceae',         # Poppy family
        'caprifoliaceae',       # Honeysuckle family
        'ericaceae',            # Heath family
        'primulaceae',          # Primrose family
        'oleaceae',             # Olive family
        'salicaceae',
        'caricaceae',
        'fagaceae',
        'rutaceae',
        'vitaceae',
        'pedaliaceae',
        'celastraceae',
        'moraceae',
        'cannabaceae',
        'rhamnaceae',
        'phrymaceae',
        'nelumbonaceae',
        'myrtaceae',
        'ebenaceae',
        'cornaceae',
        'ximeniaceae',
        'actinidiaceae',
        'acanthaceae',
        'balsaminaceae',
        'gesneriaceae',
        'juglandaceae',
        'anacardiaceae',
        'theaceae',
        'cleomaceae',
        'vitaceae',
        'proteaceae',
        'lythraceae',
        'celastraceae',
        'nymphaeaceae',
        'phrymaceae',
        'cornaceae',
        'ximeniaceae',
        'betulaceae',
        'lentibulariaceae',
        'dipterocarpaceae',
        'tropaeolaceae',
        'orobanchaceae',
        'dilleniaceae',
        'urticaceae',
        'sapindaceae',
        'combretaceae',
        'passifloraceae',
        'paeoniaceae',
        'quillajaceae',
        'meliaceae',
        'paeoniaceae',
        'myricaceae',
        'elaeagnaceae',
        'phyllanthaceae',
        'nitrariaceae',
        'bignoniaceae',
        'eucommiaceae',
        'linderniaceae',
        'cephalotaceae',
        'araliaceae',
        'ulmaceae',
        'berberidaceae',
        'gentianaceae',
        'tamaricaceae',
        'platanaceae',
        'podostemaceae',
    }


     # Common Magnoliids families
    magnoliids_families = {
        'lauraceae',   # lauraceae family
        'annonaceae',
        'aristolochiaceae',
        'magnoliaceae',
 
    }
    
    

    # Common Amborellales families
    amborellales_families = {
        'amborellaceae', 

        
    }



    # Common gymnospermae families
    gymnospermae_families = {
        'pinaceae', 
        'cupressaceae',
        'araucariaceae',

        
    }


    
    # Common lycopodiasida families
    lycopodiasida_families = {
        'selaginellaceae',   # Lycopod family
 
    }
    
    
     # Common bryopsida families
    bryopsida_families = {
        'funariaceae', 
 
    }
    
     # Common liverworts families
    marchantiopsida_families = {
        'marchantiaceae', 
 
    }
    
    
     # Common 	Polypodiopsida families
    polypodiopsida_families = {
        'equisetaceae', 
 
    }
    
    
    
     # Common Charophyta families
    charophyta_families = {
        'klebsormidiaceae', 
        'haematococcus',
        'tetrabaenaceae',
        'bathycoccaceae',
        'pyramimonadaceae',
        'haematococcaceae',
        'desmidiaceae',
        'scenedesmaceae',
        'coleochaetaceae',
 
    }
    
     # Common Chlorophyta families
    chlorophyta_families = {
        'chlorellaceae', 
        'chlorodendraceae',
        'trebouxiaceae',

 
    }
    
    
    
    if family in monocot_families:
        return 'Monocotyledon'
    elif family in dicot_families:
        return 'Dicotyledon'
    elif family in amborellales_families:
        return 'Amborellales'
    elif family in magnoliids_families:
        return 'Magnoliids'
    elif family in gymnospermae_families:
        return 'Gymnosperm'
    elif family in lycopodiasida_families:
        return 'Lycopodiasida'
    elif family in bryopsida_families:
        return 'Bryopsida'
    elif family in marchantiopsida_families:
        return 'Marchantiopsida_liverworts'
    elif family in polypodiopsida_families:
        return 'Polypodiopsida'
    elif family in charophyta_families:
        return 'Charophyta'
    elif family in chlorophyta_families:
        return 'Chlorophyta'
    else:
        return 'Unknown/Not a plant family'

def process_organism_csv(input_file, output_file, organism_column='species',  # Replace the column name containing species names
                        family_column='family', keep_all_columns=True):   # Replace the column name containing family names
    """
    Process CSV file with organism names to classify their families as monocot or dicot.
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to output CSV file
        organism_column (str): Name of the column containing organism names
        family_column (str): Name of the column containing family names
        keep_all_columns (bool): Whether to keep all original columns
    """
    
    try:
        # Read the CSV file
        print(f"Reading data from {input_file}...")
        df = pd.read_csv(input_file)
        
        # Check if required columns exist
        missing_columns = []
        if organism_column not in df.columns:
            missing_columns.append(organism_column)
        if family_column not in df.columns:
            missing_columns.append(family_column)
        
        if missing_columns:
            print(f"Error: Column(s) {missing_columns} not found in the CSV file.")
            print(f"Available columns: {list(df.columns)}")
            return None
        
        print(f"Found {len(df)} organisms to process.")
        print(f"Using organism column: '{organism_column}'")
        print(f"Using family column: '{family_column}'")
        
        # Apply classification to the family column
        print("Classifying families...")
        df['Cotyledon_Type'] = df[family_column].apply(classify_cotyledon_type)
        
        # Create summary statistics
        classification_counts = df['Cotyledon_Type'].value_counts()
        print("\nClassification Summary:")
        for classification, count in classification_counts.items():
            print(f"  {classification}: {count}")
        
        # Show some examples of each type
        print("\nExamples by classification:")
        for classification in classification_counts.index:
            examples = df[df['Cotyledon_Type'] == classification][[organism_column, family_column]].head(3)
            print(f"\n{classification}:")
            for _, row in examples.iterrows():
                print(f"  {row[organism_column]} ({row[family_column]})")
        
        # Prepare output dataframe
        if keep_all_columns:
            # Keep all original columns plus the new classification
            output_df = df.copy()
        else:
            # Keep only essential columns
            output_df = df[[organism_column, family_column, 'Cotyledon_Type']].copy()
        
        # Reorder columns to put organism first, then family, then classification
        cols = list(output_df.columns)
        if organism_column in cols and family_column in cols:
            # Remove and reinsert to get desired order
            cols.remove(organism_column)
            cols.remove(family_column)
            cols.remove('Cotyledon_Type')
            new_order = [organism_column, family_column, 'Cotyledon_Type'] + cols
            output_df = output_df[new_order]
        
        # Save results to output CSV
        print(f"\nSaving results to {output_file}...")
        output_df.to_csv(output_file, index=False)
        print(f"Successfully saved {len(output_df)} rows to {output_file}")
        
        # Display first few rows of results
        print(f"\nFirst 5 rows of results:")
        display_cols = [organism_column, family_column, 'Cotyledon_Type']
        print(output_df[display_cols].head())
        
        return output_df
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return None

def analyze_classification_results(df, organism_col='organism', family_col='family'):
    """
    Provide detailed analysis of classification results.
    """
    if df is None:
        return
    
    print("\n" + "="*60)
    print("DETAILED CLASSIFICATION ANALYSIS")
    print("="*60)
    
    # Overall statistics
    total_organisms = len(df)
    monocots = len(df[df['Cotyledon_Type'] == 'Monocotyledon'])
    dicots = len(df[df['Cotyledon_Type'] == 'Dicotyledon'])
    amborellales = len(df[df['Cotyledon_Type'] == 'Amborellales'])
    magnoliids = len(df[df['Cotyledon_Type'] == 'Magnoliids'])
    gymnosperm = len(df[df['Cotyledon_Type'] == 'Gymnosperm'])
    lycopodiasida = len(df[df['Cotyledon_Type'] == 'Lycopodiasida'])
    bryopsida = len(df[df['Cotyledon_Type'] == 'Bryopsida'])
    marchantiopsida_liverworts = len(df[df['Cotyledon_Type'] == 'Marchantiopsida_liverworts'])
    polypodiopsida = len(df[df['Cotyledon_Type'] == 'Polypodiopsida'])
    charophyta = len(df[df['Cotyledon_Type'] == 'Charophyta'])
    chlorophyta = len(df[df['Cotyledon_Type'] == 'Chlorophyta'])
    unknown = len(df[df['Cotyledon_Type'] == 'Unknown/Not a plant family'])
    
    print(f"Total organisms processed: {total_organisms}")
    print(f"Monocotyledons: {monocots} ({monocots/total_organisms*100:.1f}%)")
    print(f"Dicotyledons: {dicots} ({dicots/total_organisms*100:.1f}%)")
    print(f"Amborellales: {amborellales} ({amborellales/total_organisms*100:.1f}%)")
    print(f"Magnoliids: {magnoliids} ({magnoliids/total_organisms*100:.1f}%)")
    print(f"Gymnosperm: {gymnosperm} ({gymnosperm/total_organisms*100:.1f}%)")
    print(f"Lycopodiasida: {lycopodiasida} ({lycopodiasida/total_organisms*100:.1f}%)")
    print(f"Bryopsida: {bryopsida} ({bryopsida/total_organisms*100:.1f}%)")
    print(f"Marchantiopsida_liverworts: {marchantiopsida_liverworts} ({marchantiopsida_liverworts/total_organisms*100:.1f}%)")
    print(f"Polypodiopsida: {polypodiopsida} ({polypodiopsida/total_organisms*100:.1f}%)")
    print(f"Charophyta: {charophyta} ({charophyta/total_organisms*100:.1f}%)")
    print(f"Chlorophyta: {chlorophyta} ({chlorophyta/total_organisms*100:.1f}%)")
    print(f"Unknown/Unclassified: {unknown} ({unknown/total_organisms*100:.1f}%)")
    
    # Family breakdown
    print(f"\nFamily distribution:")
    family_counts = df.groupby([family_col, 'Cotyledon_Type']).size().unstack(fill_value=0)
    print(family_counts)
    
    # Unknown families
    if unknown > 0:
        print(f"\nUnknown/Unclassified families:")
        unknown_families = df[df['Cotyledon_Type'] == 'Unknown/Not a plant family'][family_col].unique()
        for fam in unknown_families:
            count = len(df[(df[family_col] == fam) & (df['Cotyledon_Type'] == 'Unknown/Not a plant family')])
            print(f"  {fam}: {count} organism(s)")

# Main execution - MODIFY THESE PATHS AND COLUMN NAMES
if __name__ == "__main__":
    print("Plant Organism Cotyledon Classifier")
    print("="*40)
    
    # MODIFY THESE PATHS TO YOUR ACTUAL FILE PATHS
    input_file = "/Users/winniehsiung/Protein sequence.csv"    # Replace with the file path of your datasheet
    output_file = "/Users/winniehsiung/Protein sequence_classified_organisms.csv"    # Replace with the file path of the result file
    
    # MODIFY THESE COLUMN NAMES TO MATCH YOUR CSV
    organism_col = "Organism"  # Column name containing species names
    family_col = "family"     # Column name containing family names
    
    # OPTIONS
    keep_all_columns = True   # Set to False if you only want organism, family, and cotyledon type columns
    show_detailed_analysis = True  # Set to False if you don't want detailed analysis
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        exit(1)
    
    # Process the file
    result_df = process_organism_csv(input_file, output_file, organism_col, family_col, keep_all_columns)
    
    # Detailed analysis
    if result_df is not None and show_detailed_analysis:
        analyze_classification_results(result_df, organism_col, family_col)
    
    print("\nProcessing complete!")




# ------------------------------------- This is the second code with family counts -------------------------------------------------
#%%
# Use family names to know monocots, dicots, gynosperm, etc 
# Add organism types in each famiy count
# work

import pandas as pd
import os

def classify_cotyledon_type(family_name):
    """
    Classify plant families as monocotyledon or dicotyledon.
    
    Args:
        family_name (str): Name of the plant family
        
    Returns:
        str: 'Monocotyledon', 'Dicotyledon', or 'Unknown/Not a plant family'
    """
    
    # Handle NaN or empty values
    if pd.isna(family_name) or family_name == '':
        return 'Unknown/Not a plant family'
    
    # Convert to lowercase for case-insensitive matching
    family = str(family_name).lower().strip()

    
    # Common monocotyledon families
    comid_monocot_families = {
        'poaceae',
        'arecaceae', 'palmae',  # Palm family
        'bromeliaceae',         # Bromeliad family
        'cyperaceae',           # Sedge family
        'juncaceae',            # Rush family
        'commelinaceae',        # Spiderwort family
        'haemodoraceae',
        'hanguanaceae',
        'philydraceae',
        'pontederiaceae',
        'cannaceae',
        'zingiberaceae',        # Ginger family
        'costaceae',
        'heliconiaceae',
        'lowiaceae',
        'musaceae',             # Banana family
        'strelitziaceae',
        'typhaceae',            # Cattail family
        'ecdeiocoleaceae',
        'eriocaulaceae',
        'flagellariaceae',
        'joinvilleaceae',
        'mayacaceae',
        'rapateaceae',
        'restionaceae',
        'thurniaceae',
        'xyridaceae'

    }
    

    
    # Common monocotyledon families
    noncomid_monocot_families = {
        'gramineae',  # Grass family
        'orchidaceae',           # Orchid family
        'liliaceae',            # Lily family
        'amaryllidaceae',       # Amaryllis family
        'iridaceae',            # Iris family
        'asparagaceae',         # Asparagus family
        'alliaceae',            # Onion family
        'hydrocharitaceae',     # Tape-grass family
        'alismataceae',         # Water-plantain family
        'pandanaceae',          # Screw-pine family
        'dioscoreaceae',        # Yam family
        'zosteraceae',
        'acoraceae',
        'hyacinthaceae',
        'araceae',              # Arum family
    }
    
    # Common dicotyledon families
    dicot_families = {
        'rosaceae',             # Rose family
        'fabaceae', 'leguminosae',  # Pea/Bean family
        'asteraceae', 'compositae',  # Sunflower/Daisy family
        'brassicaceae', 'cruciferae',  # Mustard family
        'solanaceae',           # Nightshade family
        'lamiaceae', 'labiatae',  # Mint family
        'apiaceae', 'umbelliferae',  # Carrot family
        'malvaceae',            # Mallow family
        'euphorbiaceae',        # Spurge family
        'rubiaceae',            # Coffee family
        'scrophulariaceae',     # Figwort family
        'ranunculaceae',        # Buttercup family
        'caryophyllaceae',      # Pink family
        'polygonaceae',         # Buckwheat family
        'convolvulaceae',       # Morning glory family
        'boraginaceae',         # Borage family
        'plantaginaceae',       # Plantain family
        'onagraceae',           # Evening primrose family
        'geraniaceae',          # Geranium family
        'violaceae',            # Violet family
        'cucurbitaceae',        # Gourd family
        'amaranthaceae',        # Amaranth family
        'chenopodiaceae',       # Goosefoot family
        'papaveraceae',         # Poppy family
        'caprifoliaceae',       # Honeysuckle family
        'ericaceae',            # Heath family
        'primulaceae',          # Primrose family
        'oleaceae',             # Olive family
        'salicaceae',
        'caricaceae',
        'fagaceae',
        'rutaceae',
        'vitaceae',
        'pedaliaceae',
        'celastraceae',
        'moraceae',
        'cannabaceae',
        'rhamnaceae',
        'phrymaceae',
        'nelumbonaceae',
        'myrtaceae',
        'ebenaceae',
        'cornaceae',
        'ximeniaceae',
        'actinidiaceae',
        'acanthaceae',
        'balsaminaceae',
        'gesneriaceae',
        'juglandaceae',
        'anacardiaceae',
        'theaceae',
        'cleomaceae',
        'proteaceae',
        'lythraceae',
        'nymphaeaceae',
        'betulaceae',
        'lentibulariaceae',
        'dipterocarpaceae',
        'tropaeolaceae',
        'orobanchaceae',
        'dilleniaceae',
        'urticaceae',
        'sapindaceae',
        'combretaceae',
        'passifloraceae',
        'paeoniaceae',
        'quillajaceae',
        'meliaceae',
        'myricaceae',
        'elaeagnaceae',
        'phyllanthaceae',
        'nitrariaceae',
        'bignoniaceae',
        'eucommiaceae',
        'linderniaceae',
        'cephalotaceae',
        'araliaceae',
        'ulmaceae',
        'berberidaceae',
        'gentianaceae',
        'tamaricaceae',
        'platanaceae',
        'podostemaceae',
    }

     # Common Magnoliids families
    magnoliids_families = {
        'lauraceae',   # lauraceae family
        'annonaceae',
        'aristolochiaceae',
        'magnoliaceae',
    }

    # Common Amborellales families
    amborellales_families = {
        'amborellaceae', 
    }

    # Common gymnospermae families
    gymnospermae_families = {
        'pinaceae', 
        'cupressaceae',
        'araucariaceae',
    }

    # Common lycopodiasida families
    lycopodiasida_families = {
        'selaginellaceae',   # Lycopod family
    }
    
     # Common bryopsida families
    bryopsida_families = {
        'funariaceae', 
    }
    
     # Common liverworts families
    marchantiopsida_families = {
        'marchantiaceae', 
    }
    
     # Common 	Polypodiopsida families
    polypodiopsida_families = {
        'equisetaceae', 
    }
    
     # Common Charophyta families
    charophyta_families = {
        'klebsormidiaceae', 
        'haematococcus',
        'tetrabaenaceae',
        'bathycoccaceae',
        'pyramimonadaceae',
        'haematococcaceae',
        'desmidiaceae',
        'scenedesmaceae',
        'coleochaetaceae',
    }
    
     # Common Chlorophyta families
    chlorophyta_families = {
        'chlorellaceae', 
        'chlorodendraceae',
        'trebouxiaceae',
        'Coccomyxaceae',
    }
    
    if family in comid_monocot_families:
        return 'Commelinid Monocotyledon'
    elif family in noncomid_monocot_families:
        return 'Non-Commelinid Monocotyledon'
    elif family in dicot_families:
        return 'Dicotyledon'
    elif family in amborellales_families:
        return 'Amborellales'
    elif family in magnoliids_families:
        return 'Magnoliids'
    elif family in gymnospermae_families:
        return 'Gymnosperm'
    elif family in lycopodiasida_families:
        return 'Lycopodiasida'
    elif family in bryopsida_families:
        return 'Bryopsida'
    elif family in marchantiopsida_families:
        return 'Marchantiopsida - liverworts'
    elif family in polypodiopsida_families:
        return 'Polypodiopsida'
    elif family in charophyta_families:
        return 'Charophyta'
    elif family in chlorophyta_families:
        return 'Chlorophyta'
    else:
        return 'Unknown/Not a plant family'

def count_organism_types_per_cotyledon_type(df, organism_column):
    """
    Count how many unique organism types are in each Cotyledon_Type classification.
    """
    # Filter out NaN values
    df_clean = df.dropna(subset=[organism_column])
    
    # Group by Cotyledon_Type and count unique organisms
    cotyledon_organism_counts = df_clean.groupby('Cotyledon_Type')[organism_column].nunique().reset_index()
    cotyledon_organism_counts.columns = ['Cotyledon_Type', 'Organism_Type_Count']
    
    # Sort by count in descending order
    cotyledon_organism_counts = cotyledon_organism_counts.sort_values('Organism_Type_Count', ascending=False)
    
    return cotyledon_organism_counts

def count_organism_types_per_family(df, organism_column, family_column):
    """
    Count how many unique organism types are in each family.
    """
    # Filter out NaN values before grouping
    df_clean = df.dropna(subset=[family_column, organism_column])
    
    # Group by family and count unique organisms
    family_organism_counts = df_clean.groupby(family_column)[organism_column].nunique().reset_index()
    family_organism_counts.columns = [family_column, 'Organism_Type_Count']
    
    # Sort by count in descending order
    family_organism_counts = family_organism_counts.sort_values('Organism_Type_Count', ascending=False)
    
    return family_organism_counts

def create_family_summary_report(df, organism_column, family_column, output_file_prefix):
    """
    Create a comprehensive family summary report with organism counts and classifications.
    """
    # Filter out NaN values
    df_clean = df.dropna(subset=[family_column, organism_column])
    
    # Count organism types per family
    family_counts = count_organism_types_per_family(df_clean, organism_column, family_column)
    
    # Add classification information for each family
    family_classification = df_clean.groupby(family_column)['Cotyledon_Type'].first().reset_index()
    
    # Merge the counts with classifications
    family_summary = pd.merge(family_counts, family_classification, on=family_column, how='left')
    
    # Add detailed organism list for each family
    organism_lists = df_clean.groupby(family_column)[organism_column].apply(
        lambda x: '; '.join(sorted(x.unique()))
    ).reset_index()
    organism_lists.columns = [family_column, 'Organism_List']
    
    # Final merge to create comprehensive summary
    family_summary = pd.merge(family_summary, organism_lists, on=family_column, how='left')
    
    # Reorder columns
    family_summary = family_summary[[family_column, 'Organism_Type_Count', 'Cotyledon_Type', 'Organism_List']]
    
    # Save family summary report
    family_report_file = f"{output_file_prefix}_family_summary.csv"
    family_summary.to_csv(family_report_file, index=False)
    
    print(f"\nFamily Summary Report saved to: {family_report_file}")
    
    return family_summary

def create_cotyledon_type_summary_report(df, organism_column, family_column, output_file_prefix):
    """
    Create a comprehensive cotyledon type summary report with organism counts and family details.
    """
    # Filter out NaN values
    df_clean = df.dropna(subset=[family_column, organism_column])
    
    # Count organism types per cotyledon type
    cotyledon_counts = count_organism_types_per_cotyledon_type(df_clean, organism_column)
    
    # Add family count information for each cotyledon type
    family_counts_per_cotyledon = df_clean.groupby('Cotyledon_Type')[family_column].nunique().reset_index()
    family_counts_per_cotyledon.columns = ['Cotyledon_Type', 'Family_Count']
    
    # Merge organism counts with family counts
    cotyledon_summary = pd.merge(cotyledon_counts, family_counts_per_cotyledon, on='Cotyledon_Type', how='left')
    
    # Add detailed organism list for each cotyledon type
    organism_lists = df_clean.groupby('Cotyledon_Type')[organism_column].apply(
        lambda x: '; '.join(sorted(x.unique()))
    ).reset_index()
    organism_lists.columns = ['Cotyledon_Type', 'Organism_List']
    
    # Add detailed family list for each cotyledon type
    family_lists = df_clean.groupby('Cotyledon_Type')[family_column].apply(
        lambda x: '; '.join(sorted(x.unique()))
    ).reset_index()
    family_lists.columns = ['Cotyledon_Type', 'Family_List']
    
    # Final merges to create comprehensive summary
    cotyledon_summary = pd.merge(cotyledon_summary, organism_lists, on='Cotyledon_Type', how='left')
    cotyledon_summary = pd.merge(cotyledon_summary, family_lists, on='Cotyledon_Type', how='left')
    
    # Reorder columns
    cotyledon_summary = cotyledon_summary[['Cotyledon_Type', 'Organism_Type_Count', 'Family_Count', 'Organism_List', 'Family_List']]
    
    # Save cotyledon type summary report
    cotyledon_report_file = f"{output_file_prefix}_cotyledon_type_summary.csv"
    cotyledon_summary.to_csv(cotyledon_report_file, index=False)
    
    print(f"Cotyledon Type Summary Report saved to: {cotyledon_report_file}")
    
    return cotyledon_summary

def process_organism_csv(input_file, output_file, organism_column='organism', 
                        family_column='family', keep_all_columns=True):
    """
    Process CSV file with organism names to classify their families as monocot or dicot.
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to output CSV file
        organism_column (str): Name of the column containing organism names
        family_column (str): Name of the column containing family names
        keep_all_columns (bool): Whether to keep all original columns
    """
    
    try:
        # Read the CSV file
        print(f"Reading data from {input_file}...")
        df = pd.read_csv(input_file)
        
        # Check if required columns exist
        missing_columns = []
        if organism_column not in df.columns:
            missing_columns.append(organism_column)
        if family_column not in df.columns:
            missing_columns.append(family_column)
        
        if missing_columns:
            print(f"Error: Column(s) {missing_columns} not found in the CSV file.")
            print(f"Available columns: {list(df.columns)}")
            return None
        
        print(f"Found {len(df)} organisms to process.")
        print(f"Using organism column: '{organism_column}'")
        print(f"Using family column: '{family_column}'")
        
        # Apply classification to the family column
        print("Classifying families...")
        df['Cotyledon_Type'] = df[family_column].apply(classify_cotyledon_type)
        
        # Create summary statistics
        classification_counts = df['Cotyledon_Type'].value_counts()
        print("\nClassification Summary:")
        for classification, count in classification_counts.items():
            print(f"  {classification}: {count}")
        
        # Show some examples of each type
        print("\nExamples by classification:")
        for classification in classification_counts.index:
            examples = df[df['Cotyledon_Type'] == classification][[organism_column, family_column]].head(3)
            print(f"\n{classification}:")
            for _, row in examples.iterrows():
                print(f"  {row[organism_column]} ({row[family_column]})")
        
        # Count organism types per family
        print("\n" + "="*60)
        print("ORGANISM TYPES PER FAMILY ANALYSIS")
        print("="*60)
        
        family_counts = count_organism_types_per_family(df, organism_column, family_column)
        
        print(f"\nTop 10 families with most organism types:")
        print(family_counts.head(10).to_string(index=False))
        
        print(f"\nTotal families analyzed: {len(family_counts)}")
        print(f"Average organism types per family: {family_counts['Organism_Type_Count'].mean():.2f}")
        print(f"Median organism types per family: {family_counts['Organism_Type_Count'].median():.1f}")
        
        # Count organism types per cotyledon type
        print("\n" + "="*60)
        print("ORGANISM TYPES PER COTYLEDON TYPE ANALYSIS")
        print("="*60)
        
        cotyledon_counts = count_organism_types_per_cotyledon_type(df, organism_column)
        
        print(f"\nOrganism types per cotyledon classification:")
        print(cotyledon_counts.to_string(index=False))
        
        # Additional statistics for cotyledon types
        family_counts_per_cotyledon = df.groupby('Cotyledon_Type')[family_column].nunique()
        print(f"\nNumber of families per cotyledon classification:")
        for cotyledon_type, family_count in family_counts_per_cotyledon.items():
            organism_count = cotyledon_counts[cotyledon_counts['Cotyledon_Type'] == cotyledon_type]['Organism_Type_Count'].iloc[0]
            print(f"  {cotyledon_type}: {organism_count} organism types across {family_count} families")
        
        # Create comprehensive reports
        output_prefix = output_file.rsplit('.', 1)[0]  # Remove .csv extension
        family_summary = create_family_summary_report(df, organism_column, family_column, output_prefix)
        cotyledon_summary = create_cotyledon_type_summary_report(df, organism_column, family_column, output_prefix)
        
        # Prepare output dataframe
        if keep_all_columns:
            # Keep all original columns plus the new classification
            output_df = df.copy()
        else:
            # Keep only essential columns
            output_df = df[[organism_column, family_column, 'Cotyledon_Type']].copy()
        
        # Reorder columns to put organism first, then family, then classification
        cols = list(output_df.columns)
        if organism_column in cols and family_column in cols:
            # Remove and reinsert to get desired order
            cols.remove(organism_column)
            cols.remove(family_column)
            cols.remove('Cotyledon_Type')
            new_order = [organism_column, family_column, 'Cotyledon_Type'] + cols
            output_df = output_df[new_order]
        
        # Save results to output CSV
        print(f"\nSaving results to {output_file}...")
        output_df.to_csv(output_file, index=False)
        print(f"Successfully saved {len(output_df)} rows to {output_file}")
        
        # Display first few rows of results
        print(f"\nFirst 5 rows of results:")
        display_cols = [organism_column, family_column, 'Cotyledon_Type']
        print(output_df[display_cols].head())
        
        return output_df
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return None

def analyze_classification_results(df, organism_col='organism', family_col='family'):
    """
    Provide detailed analysis of classification results.
    """
    if df is None:
        return
    
    print("\n" + "="*60)
    print("DETAILED CLASSIFICATION ANALYSIS")
    print("="*60)
    
    # Overall statistics
    total_organisms = len(df)
    comid_monocots = len(df[df['Cotyledon_Type'] == 'Commelinid Monocotyledon'])
    noncomid_monocots = len(df[df['Cotyledon_Type'] == 'Non-Commelinid Monocotyledon'])
    dicots = len(df[df['Cotyledon_Type'] == 'Dicotyledon'])
    amborellales = len(df[df['Cotyledon_Type'] == 'Amborellales'])
    magnoliids = len(df[df['Cotyledon_Type'] == 'Magnoliids'])
    gymnosperm = len(df[df['Cotyledon_Type'] == 'Gymnosperm'])
    lycopodiasida = len(df[df['Cotyledon_Type'] == 'Lycopodiasida'])
    bryopsida = len(df[df['Cotyledon_Type'] == 'Bryopsida'])
    marchantiopsida_liverworts = len(df[df['Cotyledon_Type'] == 'Marchantiopsida - liverworts'])
    polypodiopsida = len(df[df['Cotyledon_Type'] == 'Polypodiopsida'])
    charophyta = len(df[df['Cotyledon_Type'] == 'Charophyta'])
    chlorophyta = len(df[df['Cotyledon_Type'] == 'Chlorophyta'])
    unknown = len(df[df['Cotyledon_Type'] == 'Unknown/Not a plant family'])
    
    print(f"Total organisms processed: {total_organisms}")
    print(f"Commelinid Monocotyledons: {comid_monocots} ({comid_monocots/total_organisms*100:.1f}%)")
    print(f"Non-Commelinid Monocotyledons: {noncomid_monocots} ({noncomid_monocots/total_organisms*100:.1f}%)")
    print(f"Dicotyledons: {dicots} ({dicots/total_organisms*100:.1f}%)")
    print(f"Amborellales: {amborellales} ({amborellales/total_organisms*100:.1f}%)")
    print(f"Magnoliids: {magnoliids} ({magnoliids/total_organisms*100:.1f}%)")
    print(f"Gymnosperm: {gymnosperm} ({gymnosperm/total_organisms*100:.1f}%)")
    print(f"Lycopodiasida: {lycopodiasida} ({lycopodiasida/total_organisms*100:.1f}%)")
    print(f"Bryopsida: {bryopsida} ({bryopsida/total_organisms*100:.1f}%)")
    print(f"Marchantiopsida - liverworts: {marchantiopsida_liverworts} ({marchantiopsida_liverworts/total_organisms*100:.1f}%)")
    print(f"Polypodiopsida: {polypodiopsida} ({polypodiopsida/total_organisms*100:.1f}%)")
    print(f"Charophyta: {charophyta} ({charophyta/total_organisms*100:.1f}%)")
    print(f"Chlorophyta: {chlorophyta} ({chlorophyta/total_organisms*100:.1f}%)")
    print(f"Unknown/Unclassified: {unknown} ({unknown/total_organisms*100:.1f}%)")
    
    # Unique organism type counts per cotyledon type
    print(f"\nUnique organism types per cotyledon classification:")
    cotyledon_organism_counts = df.groupby('Cotyledon_Type')[organism_col].nunique()
    for cotyledon_type, unique_organisms in cotyledon_organism_counts.items():
        total_entries = len(df[df['Cotyledon_Type'] == cotyledon_type])
        print(f"  {cotyledon_type}: {unique_organisms} unique organism types ({total_entries} total entries)")
    
    # Family breakdown
    print(f"\nFamily distribution:")
    family_counts = df.groupby([family_col, 'Cotyledon_Type']).size().unstack(fill_value=0)
    print(family_counts)
    
    # Unknown families
    if unknown > 0:
        print(f"\nUnknown/Unclassified families:")
        unknown_families = df[df['Cotyledon_Type'] == 'Unknown/Not a plant family'][family_col].unique()
        for fam in unknown_families:
            count = len(df[(df[family_col] == fam) & (df['Cotyledon_Type'] == 'Unknown/Not a plant family')])
            unique_organisms = df[(df[family_col] == fam) & (df['Cotyledon_Type'] == 'Unknown/Not a plant family')][organism_col].nunique()
            print(f"  {fam}: {unique_organisms} unique organism types ({count} total entries)")

# Main execution - MODIFY THESE PATHS AND COLUMN NAMES
if __name__ == "__main__":
    print("Plant Organism Cotyledon Classifier")
    print("="*40)
    
    # MODIFY THESE PATHS TO YOUR ACTUAL FILE PATHS
    input_file = "/Users/winniehsiung/Protein sequence.csv"      # Replace with the file path of your datasheet
    output_file = "/Users/winniehsiung/Protein sequence_classified_organisms.csv"        # Replace with the file path of the saved result file
    
    # MODIFY THESE COLUMN NAMES TO MATCH YOUR CSV
    organism_col = "Organism"  # Column name containing species names
    family_col = "family"     # Column name containing family names
    
    # OPTIONS
    keep_all_columns = True   # Set to False if you only want organism, family, and cotyledon type columns
    show_detailed_analysis = True  # Set to False if you don't want detailed analysis
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        exit(1)
    
    # Process the file
    result_df = process_organism_csv(input_file, output_file, organism_col, family_col, keep_all_columns)
    
    # Detailed analysis
    if result_df is not None and show_detailed_analysis:
        analyze_classification_results(result_df, organism_col, family_col)
    
    print("\nProcessing complete!")






