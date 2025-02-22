import random
import statistics

database_id_1, database_id_2, database_id_3 = (
        "*" * 10, " My Movies Database ", "*" * 10
        )

menu_of_choices = (
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

movies_dict = {
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

def display_title(head_line_1, head_line_2, head_line_3):
    title_line = head_line_1 + head_line_2 + head_line_3
    return title_line


def display_menu(display_of_menu_points):
    menu = display_of_menu_points
    return menu


def option_1_movie_display(movies_in_dict):
    result = ""
    for key, val in movies_in_dict.items():
        result += f"{key}: {val}\n"
    return result


def option_2_movie_adding(movies_in_dict):
    user_input_adding_movie_name = input("Enter new movie name: ")
    if user_input_adding_movie_name:
        user_input_adding_movie_rating = float(input("Enter new movie rating (0-10): "))
        if user_input_adding_movie_rating:
            movies_in_dict[user_input_adding_movie_name] = user_input_adding_movie_rating
            print_info = f"movie {user_input_adding_movie_name} successfully added\n"
            return print_info


def option_3_movie_delete(movies_in_dict):
    user_input_delete_movie_name = input("Enter movie name to delete: ")
    if user_input_delete_movie_name not in movies_in_dict:
        print_info = f"Movie {user_input_delete_movie_name} does not exist in Database. "
        return print_info
    else:
        movies_dict.pop(user_input_delete_movie_name)
        print_info = f"movie {user_input_delete_movie_name} successfully deleted."
        return print_info


def option_4_movie_update(movies_in_dict):
    user_input_update_movie_name = input("Enter movie name to update: ")
    if user_input_update_movie_name not in movies_in_dict:
        print_info = f"Movie {user_input_update_movie_name} does not exist in Database.\n "
        return print_info
    else:
        user_input_update_movie_rating = float(input("Enter new movie rating (0-10): "))
        movies_dict[user_input_update_movie_name] = user_input_update_movie_rating
        print_info = f"Movie {user_input_update_movie_name} successfully updated.\n"
        return print_info


def option_5_get_stats(movies_in_dict):
    if len(movies_in_dict) == 0:
        print_info = "\nNo movies in database\n"
        return print_info
    else:
        def get_average():
            val_list = []
            average_rating = 0
            for val in movies_dict.values():
                val_list.append(val)
                average_rating = statistics.mean(val_list)
            print_average = f"\nThe average rating is: {average_rating:.2f}"
            return print_average
        average_get = get_average()


        def get_median():
            val_list = []
            for val in movies_dict.values():
                val_list.append(val)
                val_list.sort()
            val_list = val_list[::-1]
            median = len(val_list) // 2
            if len(val_list) % 2 != 0:
                print_med = f"The median value is: {val_list[median]}"
                return print_med, val_list
            else:
                median = len(val_list) // 2
                print_med = f"The median value is: {(val_list[median - 1] + val_list[median]) / 2}"
                return print_med, val_list
        med_value, values_list = get_median()


        def get_best_worst_ratings(list_of_vals):
            highest_rating = max(list_of_vals)
            lowest_rating = min(list_of_vals)
            best_list = []
            worst_list = []
            for key, value in movies_dict.items():
                if value == highest_rating:
                    best_list.append(key)
                    best_list.append(value)
                if value == lowest_rating:
                    worst_list.append(key)
                    worst_list.append(value)
            print_info_best = f"Highest Rating {best_list[1]}: movie(s) -> {", ".join(best_list[::2])}"
            print_info_worst = f"Lowest Rating {worst_list[1]}: movie(s) -> {", ".join(worst_list[::2])}\n"
            return print_info_best, print_info_worst
        get_best_movie, get_worst_movie = get_best_worst_ratings(values_list)
        print_info = f"{average_get}\n{med_value}\n{get_best_movie}\n{get_worst_movie}"
        return print_info


def option_6_pick_random_movie(movies_in_dict):
    random_item = random.choice(list(movies_in_dict.items()))
    display_random_choice = f"\n{random_item[0]}: {random_item[1]}\n"
    return display_random_choice


def option_7_search_movie(movies_in_dict):
    dict_lower_keys = {key.lower(): value for key, value in movies_in_dict.items()}
    user_input_search_movie = input("\nEnter part of movie name: \n").lower()
    print_info = ""
    for movie, rating in dict_lower_keys.items():
        if user_input_search_movie in movie:
            print_info += f"\n{movie.title()}: {rating}\n"
    return print_info


def option_8_sort_dict_by_rating(movies_in_dict):
    def sort_values(position):
        return position[1]


    def create_dict():
        sorted_by_values = sorted(movies_in_dict.items(), key = sort_values)[::-1]
        sorted_dict = dict(sorted_by_values)
        print_info = ""
        for key, val in sorted_dict.items():
            print_info += f"\n{key}: {val}"
        return print_info
    dict_create = create_dict()
    return dict_create


def get_user_input(movies_in_dict):
    user_menu_choice = int(input("Enter choice (1-8) "))
    if user_menu_choice == 1:
        print(f"\n{len(movies_in_dict)} movies in Database\n")
        option_1 = option_1_movie_display(movies_in_dict)
        return option_1
    elif user_menu_choice == 2:
        option_2 = option_2_movie_adding(movies_in_dict)
        return option_2
    elif user_menu_choice == 3:
        option_3 = option_3_movie_delete(movies_in_dict)
        return option_3
    elif user_menu_choice == 4:
        option_4 = option_4_movie_update(movies_in_dict)
        return option_4
    elif user_menu_choice == 5:
        option_5 = option_5_get_stats(movies_in_dict)
        return option_5
    elif user_menu_choice == 6:
        option_6 = option_6_pick_random_movie(movies_in_dict)
        return option_6
    elif user_menu_choice == 7:
        option_7 = option_7_search_movie(movies_in_dict)
        return option_7
    elif user_menu_choice == 8:
        option_8 = option_8_sort_dict_by_rating(movies_in_dict)
        return option_8
    else:
        print_info = "\nPress Enter and typ a number in range (1-8) "
        return print_info


def user_go_back():
    return_value = ""
    back_to_menu = input("\nPress enter to continue or press x to exit ")
    if back_to_menu != "x":
        main()
        return back_to_menu
    elif back_to_menu == "x":
        print("\nTHANK YOU FOR USING THE MOVIES DATABASE ")
        return return_value
    else:
        print("please press enter to continue or x to exit ")
        user_go_back()
        return return_value


def main():
    title_display = display_title(database_id_1, database_id_2, database_id_3)
    print(title_display)
    menu_display = display_menu(menu_of_choices)
    print(menu_display)
    user_input_get = get_user_input(movies_dict)
    print(user_input_get)
    go_back_user = user_go_back()
    print(go_back_user)


if __name__ == "__main__":
    main()
