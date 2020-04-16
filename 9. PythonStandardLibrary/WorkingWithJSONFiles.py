# JSON stands for Java Script Object Notation

import json
from pathlib import Path
movies = [
    {"id": 1, "Title": "Terminator", "year": 1989},
    {"id": 2, "Title": "Shawshank Redemption", "year": 2004}
]

data = json.dumps(movies)
print(data)
Path("Write_Text.json").write_text(data)

read = Path("Write_Text.json").read_text()
movies = json.loads(read)
print(movies)
print(movies[0])
print(movies[0]["Title"])
