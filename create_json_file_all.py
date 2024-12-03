import os

# Specify the path to the target directory
target_directory = 'path'

# Traverse the directory structure starting from target_directory'
for root, dirs, files in os.walk(target_directory):
    # If there are no subdirectories, we are at the end of a directory
    if not dirs:
        # Create an empty all-1.json file in this directory
        json_path = os.path.join(root, 'all-1.json')

        # Create the file if it doesn't exist yet
        if not os.path.exists(json_path):
            open(json_path, 'w').close()  # Create an empty file
            print(f"Created empty {json_path}")
        else:
            print(f"{json_path} already exists.")
