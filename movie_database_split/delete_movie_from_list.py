def option_3_movie_delete(dictionary_films):
    user_input_delete_movie_name = input("Enter movie name to delete: ").strip()
    if user_input_delete_movie_name not in dictionary_films:
        print_info = f"Movie {user_input_delete_movie_name} does not exist in Database. "
        return print_info
    else:
        dictionary_films.pop(user_input_delete_movie_name)
        print_info = f"movie {user_input_delete_movie_name} successfully deleted."
        return print_info