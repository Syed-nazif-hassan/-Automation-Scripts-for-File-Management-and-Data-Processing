import os


def create_language_json_in_all_dirs(root_dir):
    # Loop through all items in the root directory
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Only create the file in immediate child directories
        if dirpath == root_dir:
            continue

        # Path to the language.json file to create
        json_file_path = os.path.join(dirpath, 'language.json')

        # Check if the file already exists
        if not os.path.exists(json_file_path):
            # Create an empty language.json file in the directory
            with open(json_file_path, 'w') as f:
                pass
            print(f'Created language.json in: {dirpath}')
        else:
            print(f'language.json already exists in: {dirpath}')


if __name__ == "__main__":
    # Parent directory path
    root_directory = os.path.dirname(os.path.abspath(__file__))
    create_language_json_in_all_dirs(root_directory)
