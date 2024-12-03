import os
import json


def extract_terms_and_name(folder_path):
    # Traverse the directory
    for root, dirs, files in os.walk(folder_path):
        if 'combined.json' in files:
            combined_file_path = os.path.join(root, 'combined.json')
            with open(combined_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Extract the name
                name = data.get('name', {}).get('en', 'Unnamed')
                # Extract terms
                terms_list = []
                terms = data.get('terms', [])
                for term in terms:
                    term_en = term.get('term', {}).get('en')
                    if term_en:
                        terms_list.append(term_en)

            # Write to topic.md in the same directory
            write_terms_to_markdown(root, name, terms_list)


def write_terms_to_markdown(folder_path, name, terms):
    # Path to the topic.md file in the same directory
    topic_md_path = os.path.join(folder_path, 'topic.md')
    if os.path.exists(topic_md_path):
        with open(topic_md_path, 'a', encoding='utf-8') as f:
            # Write the name as a header
            f.write(f"### {name}\n\n")
            # Write each term
            for term in terms:
                f.write(f"- {term}\n")
    else:
        print(f"topic.md file does not exist in {folder_path}.")


# Adjust this to your specific folder path
folder_path = 'path'

extract_terms_and_name(folder_path)
