import random
from game_data import data
import art

def print_desc(data_1, data_2):
    """ Prints the data. """
    print(f"Compare A: {data_1["name"]}, a {data_1["description"]}, from {data_1["country"]}")
    print(art.vs)
    print(f"Against B: {data_2["name"]}, a {data_2["description"]}, from {data_2["country"]}")


def play_game():
    score = 0
    celeb_a = random.choice(data)
    celeb_b = random.choice(data)
    print_desc(celeb_a, celeb_b)

    while True:
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_choice == 'a' and celeb_a["follower_count"] > celeb_b["follower_count"]:
            score += 1
        elif user_choice == 'b' and celeb_a["follower_count"] < celeb_b["follower_count"]:
            score += 1
        else:
            print(f"Sorry, that's wrong. Final score {score}")
            return

        print(f"You're right! Current score: {score}")
        temp = celeb_b
        celeb_b = random.choice(data)
        celeb_a = temp

        print_desc(celeb_a, celeb_b)


play = input("Do you want to play the Higher Lower game? type 'y' for yes, 'n' for no: ").lower()

if play == 'y':
    print(art.logo)
    play_game()

