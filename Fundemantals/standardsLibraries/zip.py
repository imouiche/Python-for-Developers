
from pathlib import Path
from zipfile import ZipFile

with ZipFile("files.zip", "w") as zip:
    for p in Path("ecommerce").rglob("*.*"):
        zip.write(p)
