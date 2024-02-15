import sys
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent.parent

paths = [
    str(BASE_DIR / "apps"),
    str(BASE_DIR / "apps" / "backend"),
    str(BASE_DIR / "apps" / "model"),
]
sys.path.extend(paths)
