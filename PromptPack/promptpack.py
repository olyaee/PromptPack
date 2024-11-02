import os
import json
import argparse
from pathlib import Path

def generate_folder_structure(path):
    folder_structure = "Project Folder Structure:\n"
    
    def recurse_dir(current_path, prefix=""):
        entries = list(current_path.iterdir())
        for i, entry in enumerate(entries):
            connector = "└──" if i == len(entries) - 1 else "├──"
            folder_structure_line = f"{prefix}{connector} {entry.name}"
            nonlocal folder_structure
            folder_structure += folder_structure_line + "\n"
            
            if entry.is_dir():
                indent = "    " if i == len(entries) - 1 else "│   "
                recurse_dir(entry, prefix + indent)

    recurse_dir(Path(path))
    return folder_structure

def read_files(project_path, file_extensions=None, excluded_extensions=None, excluded_filenames=None):
    files = []
    excluded_extensions = excluded_extensions or []
    excluded_filenames = excluded_filenames or []

    for root, _, file_list in os.walk(project_path):
        for file_name in file_list:
            # Skip files with excluded extensions or specific filenames
            if any(file_name.endswith(ext) for ext in excluded_extensions) or file_name in excluded_filenames:
                print(f"Skipping excluded file: {file_name}")
                continue

            # Include only specified extensions, if any
            if not file_extensions or any(file_name.endswith(ext) for ext in file_extensions):
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        files.append((os.path.basename(file_path), f.read()))
                except (UnicodeDecodeError, FileNotFoundError, IOError) as e:
                    print(f"Skipping file due to error ({e}): {file_path}")
                    
    return files

def format_output(files, project_path):
    folder_structure = generate_folder_structure(project_path)
    user_prompt = f"{folder_structure}\n\n" 
    for file_name, file_content in files:
        separator = f"\n==== START {file_name} ====\n"
        end_separator = f"\n==== END {file_name} ====\n"
        user_prompt += f"{separator}{file_content}{end_separator}\n"
    return user_prompt

def save_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
    print(f"{filename} has been written.")

def main():
    parser = argparse.ArgumentParser(description="Process a folder and read files with a specified configuration.")
    parser.add_argument(
        "folder", 
        nargs="?", 
        default=Path.cwd(), 
        type=str, 
        help="Path to the project folder. Defaults to the current directory if not specified."
    )
    parser.add_argument(
        "--include_extensions",
        nargs="*",
        default=[],
        help="List of file extensions to include, e.g., '.py .md'."
    )
    parser.add_argument(
        "--excluded_extensions",
        nargs="*",
        default=[".lock"],
        help="List of file extensions to exclude, e.g., '.lock .pyc'."
    )
    parser.add_argument(
        "--excluded_filenames",
        nargs="*",
        default=["final_prompt.txt"],
        help="List of filenames to exclude, e.g., 'final_prompt.txt'."
    )

    args = parser.parse_args()

    project_path = args.folder

    # Read files based on command-line arguments
    files = read_files(
        project_path, 
        file_extensions=args.include_extensions, 
        excluded_extensions=args.excluded_extensions, 
        excluded_filenames=args.excluded_filenames
    )
    
    # Format main content with folder structure and files
    content = format_output(files, project_path)

    save_to_file("final_prompt.txt", content)

if __name__ == "__main__":
    main()
