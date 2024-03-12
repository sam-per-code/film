from connect import *
def list_films():
    try:
        dbCursor.execute("SELECT * FROM tblFilms ORDER BY Title DESC")

        allfilms = dbCursor.fetchall()
        for films in allfilms:
            print(films)
    except sql.OperationalError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_films()