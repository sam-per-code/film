from connect import *
def search_film():
    try:
        field = input("Search by filmID, title, yearReleased, rating, duration, genre: ")

        if field == "filmID":
            idInput = int(input("Enter filmID: "))
            dbCursor.execute("SELECT * FROM tblFilms WHERE filmID = ?", (idInput,))
            row = dbCursor.fetchone()

            if row is None:
                print(f"No film with filmID {idInput} exists")
            else:
                for aFilm in row:
                    print(aFilm)

        elif field in ["filmID", "title", "yearReleased", "rating", "duration", "genre" ]:
            strInput = input(f"Enter the value for the field {field}: ")
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE {field} LIKE '%{strInput}%'")
            rows = dbCursor.fetchall()
            if not rows:
                print(f"No film with field {field} matching {strInput}")

            elif field == "filmID" or field == "title" or field == "yearReleased" or field == "rating" or field == "duration" or field == "genre":
                for films in rows:
                    print(films)

        
        else:
            print(f"Search field {field} invalid!")
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    finally:
        print("DB operation performed")

if __name__ == "__main__":
    search_film()