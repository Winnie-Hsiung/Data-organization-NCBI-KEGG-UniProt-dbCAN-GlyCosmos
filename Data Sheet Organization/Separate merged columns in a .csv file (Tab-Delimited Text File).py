#Separate merged columns in a .csv file
#Tab-Delimited Text File

import csv

# Open the text file to read
with open('file path_input.txt', 'r') as file: #Replace your txt file
    lines = file.readlines()

# Open a CSV file to write
with open('file path_fixed file.csv', 'w', newline='', encoding='utf-8') as csvfile:  #Replace with the file path for your fixed file
    writer = csv.writer(csvfile)
    
    # Loop through each line in the text file
    for line in lines:
        # Split each line by the tab character
        row = line.strip().split('\t')
        # Write the row to the CSV
        writer.writerow(row)

print("Data has been saved to 'data.csv'")



#We sometimes download txt file of data from database, but each row is merged into one line in the txt file. Even though you convert the file to a csv file, the problem is not solved. This code is used to separate those merged columns.
