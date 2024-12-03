import os

# Specify the root directory containing the folders and .md files
target_directory = 'path'

# Iterate through the directory structure
for subdir, _, files in os.walk(target_directory):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(subdir, file)
            # Read the content of the .md file
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # Check if the first line matches the target text
            if lines and lines[0].strip() == "Some text":
                # Modify the first line
                lines[0] = "Modified text\n"

                # Write the updated content back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines)

print("Update completed.")
