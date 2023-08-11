import re

import yaml

from src.core import ExportMDPath, PdfPath, ReadmePath, YamlPath
from src.table_of_contents import generate_toc


def replace_patterns(
    project_name: str,
    markdown_fp: ReadmePath,
    yaml_fp: YamlPath,
    export_md_path: ExportMDPath,
    export_pdf_path: PdfPath | None = None,
    pattern: str | None = None,
    for_obsidian: bool = False,
) -> None:
    with open(markdown_fp.value, 'r') as md_file:
        md_data = md_file.read()

    with open(yaml_fp.value, 'r') as yaml_file:
        yaml_data: dict = yaml.safe_load(yaml_file)

    if pattern is None:
        pattern = r'\{\[(\w+)\]\}'

    def replace(match: re.Match) -> str:
        key = match.group(1)

        if key == 'TableOfContents':
            return '\n'.join(generate_toc(markdown_fp, for_obsidian))
        elif key == 'ProjectName':
            return project_name

        rv = yaml_data.get(key)
        return '' if rv is None else rv

    updated_data = re.sub(pattern, replace, md_data)

    export_md_path.value.parent.mkdir(parents=True, exist_ok=True)
    with open(export_md_path.value, 'w') as export_md_file:
        export_md_file.write(updated_data)

    if export_pdf_path is not None:
        raise NotImplementedError
