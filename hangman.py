import random
from hangman_words import word_list
from hangman_art import logo,art

print("Welcome to Py Hangman game made by komore!")
print(logo)
chosen_word = random.choice(word_list)
lives = 6
word_length = len(chosen_word)

end_of_game = False
 
display = []
for letter in chosen_word:
    display.append("_")
print(display)

while end_of_game == False:
    guess = input("Choose a letter: ").lower()
    clear()
    if guess in display:
        print(f"You have already guessed this letter {guess}")
   
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    print(display)

    if guess not in chosen_word:
        print(f"You have guessed this letter {guess} which is not in the word. You will lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
