import argparse
import os
from project_extractor import ProjectExtractor
from file_handler import FileHandler


def main():
    parser = argparse.ArgumentParser(description="Extract project structure and code to Markdown.")
    parser.add_argument("-d", "--directory", default=".", help="Directory to extract from (default: current directory)")
    parser.add_argument("-o", "--output", default="project_description.md", help="Output file name")
    parser.add_argument("-i", "--ignore", nargs="*", help="Additional patterns to ignore")
    parser.add_argument("-e", "--extensions", nargs="*", default=[".py", ".js", ".html", ".css"], help="File extensions to include")
    parser.add_argument("-el", "--use-export-list", action="store_true", help="Use to_export.txt file for specific file export")
    args = parser.parse_args()

    # Convert relative path to absolute path
    directory = os.path.abspath(args.directory)

    if args.use_export_list:
        export_list_path = os.path.join(directory, 'to_export.txt')
        if not os.path.exists(export_list_path):
            print(f"Error: {export_list_path} not found. This file is required when using --use-export-list.")
            return

        file_handler = FileHandler(export_list=export_list_path)
        extractor = ProjectExtractor(file_handler)
        extractor.extract_specific_files(directory, args.output)
    else:
        file_handler = FileHandler(args.ignore, extensions=args.extensions)
        extractor = ProjectExtractor(file_handler)
        extractor.extract_project(directory, args.output, args.extensions)

    print(f"Project extracted to {args.output}")

if __name__ == "__main__":
    main()