import os
import pandas as pd

# Define the path to your PDF files (in this case, the root of your repository)
pdf_files_path = './'

# Use the glob function to find all PDF files in the repository (regardless of their location within subfolders)
import glob
pdf_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(".pdf"):
            pdf_files.append(os.path.join(root, file))

# Create a list to hold the CSV data
csv_data = []

# Loop through each PDF and extract metadata (you can use any library or method you like)
for pdf_file in pdf_files:
    # For this example, we'll just print the filename
    csv_data.append({
        'ID': len(csv_data) + 1,
        'PDF Filename': os.path.basename(pdf_file),
    })

# If the CSV file doesn't exist, create it; otherwise, update its contents
if not os.path.exists('csv_data.csv'):
    pd.DataFrame(csv_data).to_csv('csv_data.csv', index=False)
else:
    existing_data = pd.read_csv('csv_data.csv')
    updated_data = pd.concat([existing_data, csv_data])
    updated_data.to_csv('csv_data.csv', index=False)

print("CSV data generated and saved to csv_data.csv")
