import json

# File paths
store_file = 'store.json'
put_file = 'put.json'

# Load JSON data from store.json with utf-8 encoding
with open(store_file, 'r', encoding='utf-8') as f:
    store_data = json.load(f)

# Load JSON data from put.json with utf-8 encoding
with open(put_file, 'r', encoding='utf-8') as f:
    put_data = json.load(f)

# Extract terms from put.json and append to store.json
put_terms = put_data.get('terms', [])
store_terms = store_data.get('terms', [])

# Append all terms from put.json to store.json
store_terms.extend(put_terms)

# Update the store_data with the new terms list
store_data['terms'] = store_terms

# Save updated store_data back to store.json with utf-8 encoding
with open(store_file, 'w', encoding='utf-8') as f:
    json.dump(store_data, f, indent=4)
