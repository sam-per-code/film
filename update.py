from connect import *

def update_films():
    try:

        filmID = int(input("Enter the FilmID to update a record: "))
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE FilmID = {filmID}")

        row = dbCursor.fetchone()

        if row == None:
            print(f"No entry with the FilmID {filmID} exists")
        else:
            fieldname = input("Enter the field (Title or yearReleased or Rating or Duration or Genre)")
            fieldValue = input(f"Enter the value for {fieldname}: ")

            dbCursor.execute(f"UPDATE tblFilms SET {fieldname} = ? WHERE FilmID = ?",(fieldValue, filmID))
            filmDb.commit()
            print(f"{filmID} Updated")
    
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    finally: 
        print("DB operation performed")

if __name__ == "__main__":
    update_films()