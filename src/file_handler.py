import os
import pathspec


class FileHandler:
    def __init__(self, custom_ignore_patterns=None, export_list=None, extensions=None):
        self.export_list = None
        self.extensions = extensions
        if export_list:
            with open(export_list, 'r') as f:
                self.export_list = [line.strip() for line in f if line.strip()]
        else:
            self.init_ignore_patterns(custom_ignore_patterns)

    def init_ignore_patterns(self, custom_patterns=None):
        patterns = self.load_default_ignore_patterns()
        if custom_patterns:
            patterns.extend(custom_patterns)
        self.ignore_spec = pathspec.PathSpec.from_lines(
            pathspec.patterns.GitWildMatchPattern, patterns
        )

    def load_default_ignore_patterns(self):
        default_ignore_path = os.path.join(os.path.dirname(__file__), '..', 'default_ignore.txt')
        if os.path.exists(default_ignore_path):
            with open(default_ignore_path, 'r') as f:
                return [line.strip() for line in f if line.strip() and not line.startswith('#')]
        return []

    def should_ignore(self, path: str, base_path: str) -> bool:
        relative_path = os.path.relpath(path, base_path)
        if self.export_list is not None:
            return relative_path not in self.export_list
        if self.extensions and os.path.isfile(path):
            return os.path.splitext(path)[1] not in self.extensions
        return self.ignore_spec.match_file(relative_path)

    def read_file(self, filepath: str) -> str:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"