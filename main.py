import asciiart
import gamedata
import random

def higher_or_lower():
    while True:  
        print(asciiart.higher_or_lower_logo)
        score = 0
        random_choice_1 = random.choice(gamedata.famous_people)
        random_choice_2 = random.choice(gamedata.famous_people)
        while random_choice_1 == random_choice_2:  
            random_choice_2 = random.choice(gamedata.famous_people)
        game_over = False
        while not game_over:
            print(f"Compare A: {random_choice_1['name']}, {random_choice_1['description']} From {random_choice_1['country']}")
            print(asciiart.vs_logo)
            print(f"Against B: {random_choice_2['name']}, {random_choice_2['description']} From {random_choice_2['country']}")
            user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
            if user_answer not in ['a', 'b']:
                print("Please enter a valid input ('A' or 'B').")
                continue 
            if ((random_choice_1['follower_count'] > random_choice_2['follower_count'] and user_answer == 'a') or 
                (random_choice_1['follower_count'] < random_choice_2['follower_count'] and user_answer == 'b')):
                score += 1
                print('\n' * 50)
                print(f"Correct! Your score is now {score}")
                random_choice_1 = random_choice_2
                random_choice_2 = random.choice(gamedata.famous_people)
                while random_choice_1 == random_choice_2:
                    random_choice_2 = random.choice(gamedata.famous_people)
            else:
                print(f"Incorrect! Final Score: {score}")
                game_over = True  
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

higher_or_lower()
