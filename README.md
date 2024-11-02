# PromptPack

PromptPack is a command-line tool that generates a text file representation of a folder structure, including the contents of specified files. This tool can be useful for sharing project structures and contents with AI tools.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Command-Line Arguments](#command-line-arguments)
- [Examples](#examples)
- [License](#license)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd PromptPack
   ```

2. **Install dependencies** using Poetry:
   ```bash
   poetry install
   ```

3. **Activate the virtual environment**:
   ```bash
   poetry shell
   ```

## Usage

Once installed, you can run `PromptPack` as a command-line tool. The basic syntax is:

```bash
promptpack [folder] [options]
```

If no folder is specified, it defaults to the current directory. The tool will generate a text file, `final_prompt.txt`, containing the folder structure and specified file contents.

### Command-Line Arguments

- **`folder`** (optional): Path to the folder you want to analyze. Defaults to the current directory if not specified.

- **`--include_extensions`** (optional): List of file extensions to include in the output. Example: `.py .md`. If not specified, all extensions are included except those in `excluded_extensions`.

- **`--excluded_extensions`** (optional): List of file extensions to exclude from the output. Example: `.lock .git`. Defaults to `[".lock", ".git"]`.

- **`--excluded_filenames`** (optional): List of specific filenames to exclude. Example: `final_prompt.txt .git`. Defaults to `["final_prompt.txt", ".git"]`.

### Examples

1. **Generate a folder structure and file contents for the current directory**:
   ```bash
   promptpack
   ```

2. **Specify a folder to analyze**:
   ```bash
   promptpack /path/to/project
   ```

3. **Include only Python and Markdown files**:
   ```bash
   promptpack /path/to/project --include_extensions .py .md
   ```

4. **Exclude specific extensions and filenames**:
   ```bash
   promptpack /path/to/project --excluded_extensions .lock .json --excluded_filenames README.md
   ```

### Output

The output will be saved in `final_prompt.txt`, including:
- A hierarchical folder structure view.
- The contents of files matching the criteria specified by command-line arguments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This README should help guide you and others on how to install and use `PromptPack` effectively.