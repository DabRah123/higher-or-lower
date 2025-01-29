# **Higher or Lower Game**

A simple command-line game where players guess which celebrity has more social media followers.


## **Overview**

The "Higher or Lower" game presents two famous personalities, and the player must guess which one has more social media followers. The game continues until the player makes an incorrect guess.


## **How to Play**

The game displays two famous personalities with their description and country.

The player must choose which one has a higher follower count by typing 'A' or 'B'.

If the player guesses correctly, they continue with a new opponent and gain points.

The game ends when the player makes an incorrect guess.

The final score is displayed, and the player has the option to play again.


## **Algorithm**

### **Initialize Game**

Display the game logo.

Set score = 0.

Select the first two random personalities from gamedata.famous_people, ensuring they are different.

### **Game Loop**

Display details of both choices, including name, description, and country.

Prompt the user for input ('A' or 'B').

Validate input to ensure it is either 'A' or 'B'.

Compare follower counts:

If the selected choice has more followers:

Increase score by 1.

Move the selected personality to the next round.

Select a new random opponent, ensuring it is different from the current personality.

Clear the console to refresh the display.

If the selected choice has fewer followers:

Display the final score.

Set game_over = True to exit the loop.

### **Ask to Play Again**

Prompt the user to play again ('y' or 'n').

If 'y', restart the game from the beginning.

If 'n', display a thank you message and exit.
