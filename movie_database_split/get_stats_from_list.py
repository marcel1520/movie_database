import statistics

def option_5_get_stats(dictionary_films):
    if len(dictionary_films) == 0:
        print_info = "\nNo movies in database\n"
        return print_info
    else:
        def get_average():
            val_list = []
            average_rating = 0
            for val in dictionary_films.values():
                val_list.append(val)
                average_rating = statistics.mean(val_list)
            print_average = f"\nThe average rating is: {average_rating:.2f}"
            return print_average
        average_get = get_average()


        def get_median():
            val_list = []
            for val in dictionary_films.values():
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
            for key, value in dictionary_films.items():
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