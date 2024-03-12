import add, delete, read, update, search

def read_file(file_path):
    try:
        with open(file_path) as readfile:
            rf = readfile.read()

        return rf

    except FileNotFoundError as nf:
        print(f"File not found: {nf}")


def films_menu():
    option = 0
    optionsList = ["1","2","3","4","5"]
    menu_choices = read_file("menuoptions.txt")

    while option not in optionsList:
        print(menu_choices)

        option = input("Enter an option from the menu above: ")

        if option not in optionsList:
            print(f"{option} is not a valid choice")
    return option

mainProgram = True

while mainProgram:
    main_menu = films_menu()

    match main_menu:
        case "1":
            add.add_films()
        case "2":
            delete.delete_afilm()
        case "3":
            read.print_all_films()
        case "4":
            update.update_films()
        case "5":
            search.search_film()
        case _:
            mainProgram = False
    
input("Press Enter to Exit....6")
        
    