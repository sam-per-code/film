from connect import *

def add_films():
    try:
        filmId = int(input("Enter film Id: "))
        title = input("Enter film Title: ")
        year = input("Enter film year: ")
        rating = input("Enter film rating: ")
        duration = input("Enter film duration: ")
        genre = input("Enter film genre: ")

        dbCursor.execute("INSERT INTO tblFilms VALUES(?,?,?,?,?,?)", (filmId, title, year, rating, duration, genre))
        filmDb.commit()
        print(f"{title} inserted in the film database")

    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    except sql.Error as er:
        print(f"This error occurs: {er}")

if __name__ == "__main__":

    add_films()
