def option_7_search_movie(dictionary_films):
    dict_lower_keys = {key.lower(): value for key, value in dictionary_films.items()}
    user_input_search_movie = input("\nEnter part of movie name: ").lower()
    print_info = ""
    for movie, rating in dict_lower_keys.items():
        if user_input_search_movie in movie:
            print_info += f"\n{movie.title()}: {rating}"
    return print_info