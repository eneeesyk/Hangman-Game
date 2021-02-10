import random
from hangman_stages import stages

words_list = []

with open('words.txt','r') as f:
    for line in f:
        for word in line.split():
           words_list.append(word)
f.close()

chosen_word = str(random.choice(words_list))
display = []
word_length = len(chosen_word)
game_over = False
player_lives = 6
guessed_words = []

for i in range(word_length):
    display += "_"


print("Don't forget you have only 7 lives.")
while not game_over:
    guess = input("Guess a letter: (If you want to guess the whole word type 1)\n").lower()
    if guess == '1':
        guess_word = input("Whats your entire guess? ").lower()
        if guess_word == chosen_word:
            game_over = True
            print("You win")
        else:
            print("Keep guessing it is not true")
            continue
    else:
        if guess in guessed_words:
            print(f"You already write {guess}!")
        else:
            guessed_words.append(guess)
            for pos in range(word_length):
                letter = chosen_word[pos]
                if letter == guess:
                    print(f"You guessed {guess}, nice work! ")
                    display[pos] = letter

            if guess not in chosen_word:
                player_lives -= 1
                print(f"You guessed {guess}, that's not in the word.")
                print(f"You lose a life. Remaining lives {player_lives}")
                if player_lives == 0:
                    game_over = True
                    print("You lose")
                    print(f"The word was {chosen_word}")

            print(''.join(display))

            if "_" not in display:
                game_over = True
                print("You win")

            print(stages[player_lives])