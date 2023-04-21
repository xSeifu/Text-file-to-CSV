import csv

# Set the path to your text file
txt_file = 'C:/your/path/to/.txt'

# Set the path to your CSV file
csv_file = 'C:/your/path/to/.csv'

# Set the keywords you want to search for
keywords = ['Keyword1', 'Keyword2', 'Keyword3']

# Open the text file and read its contents
with open(txt_file, 'r') as file:
    lines = file.readlines()

# Initialize the dictionary for storing the column data
columns = {keyword: [] for keyword in keywords}

# Loop through the lines of the text file and search for the keywords
for line in lines:
    for keyword in keywords:
        if keyword in line:
            # If a keyword is found, append the line after the keyword to the corresponding column list 
            columns[keyword].append(line.strip().split(keyword, 1)[1])
            break

# Write the columns to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(keywords)
    for i in range(len(lines)):
        writer.writerow([columns[keyword][i] if i < len(columns[keyword]) else '' for keyword in keywords])
