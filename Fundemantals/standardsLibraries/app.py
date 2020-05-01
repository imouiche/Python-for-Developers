
from pathlib import Path

path = Path(r"\Modules\ecommerce\__init__.py")

path.exists()
path.is_file()
path.is_dir()

print(path.name)
print(path.stem)
print(path.parent)
print(path.suffix)

#path = path.with_suffix(".txt")
# print(path.absolute())

# 3

path = Path("ecommerce")

paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.rglob("*.py")]

print(py_files)
print(paths)
