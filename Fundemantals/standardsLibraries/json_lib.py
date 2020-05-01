
import json

from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "kindergarten Cop", "year": 1993}
]

data = json.dumps(movies)
Path("movies.json").write_text(data)
# print(data)

# read

data = Path("movies.json").read_text()

movies = json.loads(data)
print(movies)
