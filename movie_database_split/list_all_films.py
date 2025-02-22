def option_1_display_dictionary(films):
    all_films = ""
    for key, val in films.items():
        all_films += f"{key} {val}\n"
    return all_films