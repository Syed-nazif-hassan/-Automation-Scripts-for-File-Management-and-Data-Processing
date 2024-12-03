import json
import os
import math

# Load the store.json data
store_file = 'store.json'
with open(store_file, 'r', encoding='utf-8') as f:
    store_data = json.load(f)

# Count how many 'term' objects are in the 'terms' list
num_terms = len(store_data['terms'])

# Extract the folder name from store.json
folder_name = store_data.get('slug')

# Define the base directory for the new folder
base_dir = 'path'

# Create the full path for the new folder using the extracted folder name
folder_path = os.path.join(base_dir, folder_name)

# Create the folder
os.makedirs(folder_path, exist_ok=True)

# Save the entire content of store.json to a new file named 'slug-main.json'
main_file_path = os.path.join(folder_path, f'{folder_name}-main.json')
with open(main_file_path, 'w', encoding='utf-8') as f:
    json.dump(store_data, f, indent=4, ensure_ascii=False)

# Calculate the number of files to create (one file for every 12 terms)
num_files = math.ceil(num_terms / 12)

# Create files in the folder, each containing up to 12 terms
for i in range(num_files):
    # Calculate the start and end indices for the current batch of terms
    start_idx = i * 12
    end_idx = min((i + 1) * 12, num_terms)

    # Extract the current batch of terms
    terms_batch = store_data['terms'][start_idx:end_idx]

    # Update the terms list in a copy of store_data
    store_data_copy = store_data.copy()
    store_data_copy['terms'] = terms_batch

    # Create a new file for this batch
    file_name = store_data.get('slug') + f'-{i+1}.json'
    file_path = os.path.join(folder_path, file_name)

    # Write the current batch of terms to the new file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(store_data_copy, f, indent=4, ensure_ascii=False)

print(f'Automation completed: {num_terms} terms processed into {
      num_files} files, in folder: {folder_name}.')
