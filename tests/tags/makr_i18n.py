import os
import re


def find_html_files(start_dir):
    """
    Recursively finds all HTML files in the given directory and its subdirectories.
    Returns a list of file paths.
    """
    html_files = []
    for dirpath, dirnames, filenames in os.walk(start_dir):
        for filename in filenames:
            if filename.endswith('.html'):
                html_files.append(os.path.join(dirpath, filename))
    return html_files


def check_i18n_attributes(html_files):
    """
    Goes through all HTML files in the given list and checks if tags p, button, h2, h
    have attribute i18n. If they don't, prints the file name and line number of the offending tag.
    """
    for file_path in html_files:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                for tag in ['p', 'button', 'h2', 'h']:
                    pattern = rf'<{tag}\s+(?!(.*\s)?i18n=[\'"])'
                    match = re.search(pattern, line)
                    if match is not None:
                        print(f'File: {file_path}, Line: {i + 1}, Tag: {tag}')
