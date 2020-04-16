import sqlite3
import json
from pathlib import Path

path = Path("Write_text.json").read_text()
movies = json.loads(path)
print(movies)
# USED FOR WRITING
# with sqlite3.connect("db.sqlite3") as connection:
#    command = "INSERT INTO Movies VALUES(?, ?, ?)"
#    for movie in movies:
#        connection.execute(command, tuple(movie.values()))
#    connection.commit()

# USED FOR WRITING
with sqlite3.connect("db.sqlite3") as connection:
    command = "SELECT * FROM Movies"
    cursor = connection.execute(command)
    for row in cursor:
        print(row)   # We can also use movies=cursor.fetchall() print(movies) intead
        # of line 19 and 20
