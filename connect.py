import sqlite3 as sql

try:

    with sql.connect("filmflix.db") as filmDb:

        dbCursor = filmDb.cursor()
        

except sql.OperationalError as e:
    print(f"connection failed {e}")