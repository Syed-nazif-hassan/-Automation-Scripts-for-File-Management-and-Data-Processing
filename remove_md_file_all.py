import os

# Specify the path to the target directory
target_directory = 'path'

# Traverse the directory structure starting from target_directory
for root, dirs, files in os.walk(target_directory):
    # If there are no subdirectories, we are at the end of a directory
    if not dirs:
        # Path to the topic.md file in this directory
        md_path = os.path.join(root, 'topic.md')

        # Check if the topic.md file exists, and if so, remove it
        if os.path.exists(md_path):
            os.remove(md_path)  # Remove the file
            print(f"Removed {md_path}")
        else:
            print(f"{md_path} does not exist.")
