from connect import *

def list_films():
    try:
        category = input("List films by which category (FilmID, Title, yearReleased, Genre): ")

        allowed_categories = ["FilmID", "Title", "yearReleased", "Genre"]
        if category not in allowed_categories:
            print("Invalid category. Please choose from FilmID, Title, yearReleased or Genre")
            return 
        
        sql_query= f"SELECT * FROM tblFilms ORDER BY {category} DESC"
        dbCursor.execute(sql_query)
        all_films = dbCursor.fetchall()

        for film in all_films:
            print(film)

    except sql.OperationalError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_films()