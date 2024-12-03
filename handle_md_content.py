import os
from pathlib import Path

# Replace 'path' with the path to the directory containing .md files
target_directory = 'path'


def extract_last_header_section(content):
    try:
        lines = content.splitlines()
        last_header = None
        bullet_points = []
        current_section_bullet_points = []

        for line in lines:
            # Check if it's a header line
            if line.startswith("#"):
                # Store the last header and its bullet points when we encounter a new header
                last_header = line
                bullet_points = current_section_bullet_points
                current_section_bullet_points = []  # Reset for the new section

            # If a bullet point is found after the last header, collect it
            elif line.startswith("-"):
                current_section_bullet_points.append(line.strip())

        # After the loop, store the bullet points from the last section
        if current_section_bullet_points:
            bullet_points = current_section_bullet_points

        return last_header, bullet_points

    except Exception as e:
        print(f"Error extracting header and bullet points: {e}")
        return None, None


def write_to_topic_md(dirpath, last_header, bullet_points):
    try:
        # Define the path for the topic.md file
        topic_md_path = Path(dirpath) / 'topic.md'

        # Check if topic.md already exists
        if topic_md_path.exists():
            print(f"File {topic_md_path} already exists, skipping creation.")
            return

        # Create and write the header and bullet points to topic.md
        with open(topic_md_path, 'w', encoding='utf-8') as topic_file:
            topic_file.write(last_header + "\n\n")
            topic_file.write("\n".join(bullet_points) + "\n")
            print(f"Created and wrote to {topic_md_path}")

    except Exception as e:
        print(f"Error writing to topic.md: {e}")


def target(directory):
    try:
        # Traverse the directory structure to find all .md files
        for dirpath, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".md"):
                    md_file_path = Path(dirpath) / file

                    # Read the .md file
                    try:
                        with open(md_file_path, 'r', encoding='utf-8') as md_file:
                            content = md_file.read()
                    except Exception as e:
                        print(f"Error reading {md_file_path}: {e}")
                        continue

                    # Extract the last header and bullet points
                    last_header, bullet_points = extract_last_header_section(
                        content)

                    if last_header and bullet_points:
                        # Write to topic.md if it doesn't exist
                        write_to_topic_md(dirpath, last_header, bullet_points)

    except Exception as e:
        print(f"Error processing directory {directory}: {e}")


if __name__ == "__main__":
    target(target_directory)
