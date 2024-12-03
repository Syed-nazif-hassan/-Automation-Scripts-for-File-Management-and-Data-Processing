import os

# Specify the path to the target directory
target_directory = 'path'

# Traverse the directory structure starting from target_directory
for root, dirs, files in os.walk(target_directory):
    # If there are no subdirectories, we are at the end of a directory
    if not dirs:
        # Create an empty topic.md file in this directory
        md_path = os.path.join(root, 'topic.md')

        # Create the file if it doesn't exist yet
        if not os.path.exists(md_path):
            open(md_path, 'w').close()  # Create an empty file
            print(f"Created empty {md_path}")
        else:
            print(f"{md_path} already exists.")
