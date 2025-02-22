import random

def option_6_pick_random_movie(dictionary_films):
    random_item = random.choice(list(dictionary_films.items()))
    display_random_choice = f"\n{random_item[0]}: {random_item[1]}\n"
    return display_random_choice