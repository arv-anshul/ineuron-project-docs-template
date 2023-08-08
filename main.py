from src.core.config import ExportMDPath, ReadmePath, YamlPath
from src.fill_pattern import replace_patterns

FILES = ['LLD', 'HLD', 'ARCHITECTURE', 'DPR', 'WIREFRAME']

def main():
    for i in FILES:
        replace_patterns(
            markdown_fp=getattr(ReadmePath, i),
            yaml_fp=getattr(YamlPath, i),
            export_md_path=getattr(ExportMDPath, i),
        )

if __name__ == '__main__':
    main()
