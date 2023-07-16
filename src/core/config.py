"""
Configuration variables, functions, classes, etc.
"""

from enum import Enum
from pathlib import Path


class ReadmePath(Enum):
    DPR = Path('docs/markdowns/DPR.md')
    ARCHITECTURE = Path('docs/markdowns/Architecture.md')
    LLD = Path('docs/markdowns/LLD.md')
    HLD = Path('docs/markdowns/HLD.md')
    WIREFRAME = Path('docs/markdowns/Wireframe.md')


class YamlPath(Enum):
    DPR = Path('docs/yaml/DPR.yaml')
    ARCHITECTURE = Path('docs/yaml/Architecture.yaml')
    LLD = Path('docs/yaml/LLD.yaml')
    HLD = Path('docs/yaml/HLD.yaml')
    WIREFRAME = Path('docs/yaml/Wireframe.yaml')


class PdfPath(Enum):
    DPR = Path('export/pdf/DPR.pdf')
    ARCHITECTURE = Path('export/pdf/Architecture.pdf')
    LLD = Path('export/pdf/LLD.pdf')
    HLD = Path('export/pdf/HLD.pdf')
    WIREFRAME = Path('export/pdf/Wireframe.pdf')


class ExportMDPath(Enum):
    DPR = Path('export/markdowns/DPR.md')
    ARCHITECTURE = Path('export/markdowns/Architecture.md')
    LLD = Path('export/markdowns/LLD.md')
    HLD = Path('export/markdowns/HLD.md')
    WIREFRAME = Path('export/markdowns/Wireframe.md')
