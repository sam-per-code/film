from connect import*

# Function to print all records in tblfilms
def print_all_films():
    try:

        allfilms = dbCursor.execute("SELECT * FROM tblFilms").fetchall()

        allfilms = dbCursor.execute("SELECT * FROM tblFilms").fetchall()
        if allfilms:
            print("filmID | title | yearReleased | rating | duration | genre")
            print("*" * 70)

        for aFilm in allfilms:
                print(f"{aFilm[0]:<5} | {aFilm[1]:<50} | {aFilm[2]:<5} | {aFilm[3]:<5} | {aFilm[4]:<10} | {aFilm[5]:<8}")

        
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because {pe}")
    finally:
        print("DB operation performed")

__name__ == "__main__"
print_all_films()