from connect import *

def delete_afilm():
    try:
        filmID = int(input("Enter the FilmID to delete record: "))
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {filmID}")

        row = dbCursor.fetchone()

        if row == None:
            print(f"FilmID {filmID} does not exist")
        else:
            dbCursor.execute("DELETE FROM tblFilms WHERE FilmID =?", (filmID,))
            filmDb.commit()
            print(f"The film {filmID} is deleted from the film database")

    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    finally:
        print("DB operation performed")

if __name__ == "__main__":
    delete_afilm()