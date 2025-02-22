import user_input_choices
import display_contents


def main():
    films_database = {
        "The Shaw_shank Redemption": 9.5,
        "Pulp Fiction": 9.5,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7,
        "Terminator: Genesys": 3.6
    }
    dictionary_films_database = display_contents.films_dictionary(films_database)
    while True:
        title_database = (
            f"\n{"*" * 10 + " MY MOVIE DATABASE " + "*" * 10}"
        )
        menu_database = (
            f"\nMOVIES DATABASE MENU:\n"
            f"1. List Movies\n"
            f"2. Add movie\n"
            f"3. Delete movie\n"
            f"4. Update movie\n"
            f"5. Stats\n"
            f"6. Random movie\n"
            f"7. Search movie\n"
            f"8. Movies sorted by rating\n"
        )
        line_header = display_contents.header(title_database)
        print(line_header)
        list_choices = display_contents.menu(menu_database)
        print(list_choices)
        user_input_get = user_input_choices.get_user_input(dictionary_films_database)
        print(user_input_get)


        if input("Press Enter key to continue or Press any key to exit ").lower():
            print("Thank you for using the Movie Database")
            break

if __name__ == "__main__":
    main()

