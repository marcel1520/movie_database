def option_8_sort_dict_by_rating(dictionary_films):
    def sort_values(position):
        return position[1]


    def create_dict():
        sorted_by_values = sorted(dictionary_films.items(), key = sort_values)[::-1]
        sorted_dict = dict(sorted_by_values)
        print_info = ""
        for key, val in sorted_dict.items():
            print_info += f"{key}: {val}\n"
        return print_info
    dict_create = create_dict()
    return dict_create