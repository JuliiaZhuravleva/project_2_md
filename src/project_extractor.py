import os
from file_handler import FileHandler

class ProjectExtractor:
    def __init__(self, file_handler: FileHandler):
        self.file_handler = file_handler

    def extract_project(self, directory: str, output_file: str, extensions: list):
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# Project Structure\n\n")
            self._write_structure(f, directory, directory)
            f.write("\n# File Contents\n\n")
            self._write_contents(f, directory, directory, extensions)

    def extract_specific_files(self, directory: str, output_file: str):
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# Specific Files Content\n\n")
            for root, _, files in os.walk(directory):
                for filename in files:
                    filepath = os.path.join(root, filename)
                    if not self.file_handler.should_ignore(filepath, directory):
                        relative_path = os.path.relpath(filepath, directory)
                        f.write(f"## {relative_path}\n\n```{self._get_language(filename)}\n")
                        f.write(self.file_handler.read_file(filepath))
                        f.write("\n```\n\n")

    def _write_structure(self, file, directory: str, base_directory: str, prefix: str = ""):
        items = sorted(os.listdir(directory))
        for index, item in enumerate(items):
            path = os.path.join(directory, item)
            if self.file_handler.should_ignore(path, base_directory):
                continue
            is_last = index == len(items) - 1
            relative_path = os.path.relpath(path, base_directory)
            file.write(f"{prefix}{'└── ' if is_last else '├── '}{relative_path}\n")
            if os.path.isdir(path):
                self._write_structure(file, path, base_directory, prefix + ("    " if is_last else "│   "))

    def _write_contents(self, file, directory: str, base_directory: str, extensions: list):
        for root, _, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                if self.file_handler.should_ignore(filepath, base_directory):
                    continue
                if os.path.splitext(filename)[1] in extensions:
                    relative_path = os.path.relpath(filepath, base_directory)
                    file.write(f"## {relative_path}\n\n```{self._get_language(filename)}\n")
                    file.write(self.file_handler.read_file(filepath))
                    file.write("\n```\n\n")

    def _get_language(self, filename: str) -> str:
        ext = os.path.splitext(filename)[1]
        return {
            '.py': 'python',
            '.js': 'javascript',
            '.html': 'html',
            '.css': 'css'
        }.get(ext, '')