"""Build the downloadable homework template zip from _hw-template/.

Renames the dotless `gitignore` in the source to `.gitignore` inside the archive
(a live `.gitignore` in the site repo would wrongly ignore the template's own
data/ folder). The source folder and this script are underscore-prefixed so
Quarto ignores them at render time. Run from anywhere:

    python assignments/_build-template-zip.py
"""
import pathlib
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "_hw-template"
OUT = HERE / "econ372-hw-template.zip"
ROOT = "econ372-hw-template"          # top-level folder students see after unzip
RENAME = {"gitignore": ".gitignore"}  # dotless in the repo, dotted in the zip

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted(SRC.rglob("*")):
        if p.is_file():
            parts = list(p.relative_to(SRC).parts)
            parts[-1] = RENAME.get(parts[-1], parts[-1])
            z.write(p, str(pathlib.PurePosixPath(ROOT, *parts)))

print(f"wrote {OUT}")
