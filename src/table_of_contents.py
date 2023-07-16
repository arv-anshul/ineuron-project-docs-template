"""
Functions which are used to get the **Table of Contents** of a Markdown file.
"""

import re

from src.core.config import ReadmePath


def generate_toc(fp: ReadmePath) -> list[str]:
    with open(fp.value, 'r') as file:
        content = file.read()

    headers = re.findall(r'^(#+)\s*(.+)$', content, flags=re.MULTILINE)

    table_of_contents = []
    for header in headers:
        level = len(header[0]) - 1
        title = header[1]
        link = re.sub(r'\s', '-', title.lower())
        link = re.sub(r'[^\w-]', '', link)

        table_of_contents.append(f"{'  '*level}- [{title}](#{link})\n")

    return table_of_contents
