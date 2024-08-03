# Project 2 MD

Project 2 MD is a command-line tool that extracts the structure and code of a project and saves it in a Markdown file. This is useful for sharing project overviews or for submitting code to Large Language Models (LLMs) in a text format.

## Installation

To install Project 2 MD, follow these steps:

1. Clone the repository:

    git clone https://github.com/yourusername/project_2_md.git
    cd project_2_md

2. Create and activate a virtual environment (optional but recommended):

python -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate

3. Install the package:

pip install -e .

## Updating

If you've already installed Project 2 MD and want to update it to the latest version, follow these steps:

1. Navigate to the project directory:

cd path/to/project_2_md

2. Pull the latest changes:

git pull origin main

3. Activate your virtual environment (if you're using one):

source .venv/bin/activate  # On Windows, use .venv\Scripts\activate

4. Reinstall the package:

pip install -e .

This will update your installation to the latest version of Project 2 MD.

## Usage

After installation, you can use the project_2_md command from your terminal:

project_2_md [OPTIONS]

### Options:

- -d, --directory DIRECTORY: The path to the project directory you want to extract (default: current directory).
- -o, --output FILENAME: Specify the output Markdown file name (default: "project_description.md").
- -i, --ignore [PATTERNS...]: Specify patterns for files or directories to ignore (in addition to default patterns).
- -e, --extensions [EXTENSIONS...]: Specify file extensions to include (default: [".py", ".js", ".html", ".css"]).
- -el, --use-export-list: Use a to_export.txt file for specific file export.

### Examples:

1. Basic usage (current directory):

project_2_md -o project_overview.md -i .venv node_modules -e .py .js

This command will:
- Extract the structure and code from the current directory
- Ignore ".venv" and "node_modules" directories (in addition to default ignore patterns)
- Include only Python (.py) and JavaScript (.js) files
- Save the output to "project_overview.md"

2. Specifying a different directory:

project_2_md -d /path/to/your/project -o project_overview.md

3. Using an export list:

project_2_md -el -o specific_files.md

This command will:
- Look for a to_export.txt file in the current directory
- Extract only the files listed in to_export.txt
- Ignore the -i and -e options if they are provided
- Save the output to "specific_files.md"

Note: The to_export.txt file should contain one relative file path per line, e.g.:

src/main.py
src/utils.py
README.md

## Features

- Extracts project structure and presents it in a tree-like format
- Includes file contents with syntax highlighting based on file extension
- Allows customization of ignored files/directories and included file extensions
- Uses a default ignore list similar to common .gitignore patterns
- Provides an option to extract only specific files listed in to_export.txt
- Can be run from any directory, defaulting to the current working directory

## Default Ignore Patterns

Project 2 MD comes with a set of default ignore patterns to exclude common temporary files, build artifacts, and environment-specific files. You can find these patterns in the default_ignore.txt file in the project root.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.