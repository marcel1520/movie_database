def option_2_movie_adding(dictionary_films):
    try:
        user_input_adding_movie_name = input("Enter new movie name: ").strip()
        if user_input_adding_movie_name:
            user_input_adding_movie_rating = float(input("Enter new movie rating (0-10): "))
            if user_input_adding_movie_rating:
                dictionary_films[user_input_adding_movie_name] = user_input_adding_movie_rating
                print_info = f"movie {user_input_adding_movie_name} successfully added\n"
                return print_info
    except ValueError:
        return "Invalid Movie rating entered "