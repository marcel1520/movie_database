import list_all_films
import add_movie_to_list
import delete_movie_from_list
import update_movie_in_list
import get_stats_from_list
import pick_random_from_list
import search_movie_in_list
import sort_list_by_ratings

def get_user_input(dictionary_films):
    try:
        user_choice = int(input("Enter choice (1-8) ")) #if press enter -> ValueError
    except ValueError:
        return "select a choice from the menu in range (1-8) "
    if user_choice == 1:
        print(f"\n{len(dictionary_films)} in the Movie Database\n")
        option_1 = list_all_films.option_1_display_dictionary(dictionary_films)
        return option_1
    elif user_choice == 2:
        option_2 = add_movie_to_list.option_2_movie_adding(dictionary_films)
        return option_2
    elif user_choice == 3:
        option_3 = delete_movie_from_list.option_3_movie_delete(dictionary_films)
        return option_3
    elif user_choice == 4:
        option_4 = update_movie_in_list.option_4_movie_update(dictionary_films)
        return option_4
    elif user_choice == 5:
        option_5 = get_stats_from_list.option_5_get_stats(dictionary_films)
        return option_5
    elif user_choice == 6:
        option_6 = pick_random_from_list.option_6_pick_random_movie(dictionary_films)
        return option_6
    elif user_choice == 7:
        option_7 = search_movie_in_list.option_7_search_movie(dictionary_films)
        return option_7
    elif user_choice == 8:
        option_8 = sort_list_by_ratings.option_8_sort_dict_by_rating(dictionary_films)
        return option_8
    else:
        print_info = "\nenter a number in range (1-8) "
        return print_info