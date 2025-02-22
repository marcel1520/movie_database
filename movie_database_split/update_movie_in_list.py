def option_4_movie_update(dictionary_films):
    user_input_update_movie_name = input("Enter movie name to update: ").strip()
    if user_input_update_movie_name not in dictionary_films:
        print_info = f"Movie {user_input_update_movie_name} does not exist in Database.\n "
        return print_info
    else:
        try:
            user_input_update_movie_rating = float(input("Enter new movie rating (0-10): "))
            dictionary_films[user_input_update_movie_name] = user_input_update_movie_rating
            print_info = f"Movie {user_input_update_movie_name} successfully updated.\n"
            return print_info
        except ValueError:
            return "Invalid Movie rating entered "