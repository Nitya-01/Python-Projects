import random
from collections import Counter

# List of words (fruits) to choose from
someWords = '''strawberry orange grape pineapple apricot lemon coconut apple watermelon cherry banana papaya berry peach muskmelon'''

# Split the words into a list
someWords = someWords.split()

# Randomly choose a word
word = random.choice(someWords)

if __name__ == '__main__':
    print('Welcome to Hangman! Guess the word! HINT: It is a name of a fruit.')
    print('You have {} chances.'.format(len(word) + 2))

    # Print initial underscores for the word to guess
    guessed_letters = set()
    chances = len(word) + 2

    try:
        while chances > 0:
            print()

            # Print the current state of the word
            display_word = ''.join([char if char in guessed_letters else '_' for char in word])
            print(display_word)

            # Check if the word has been completely guessed
            if display_word == word:
                print('Congratulations, You won!')
                break

            # Take input from the user
            guess = input('Enter a letter to guess: ').lower()

            # Validate the input
            if not guess.isalpha():
                print('Please enter only letters.')
                continue
            elif len(guess) != 1:
                print('Please enter only a single letter.')
                continue
            elif guess in guessed_letters:
                print('You have already guessed that letter.')
                continue

            # Add the guessed letter to guessed letters
            guessed_letters.add(guess)

            # Check if the guessed letter is in the word
            if guess not in word:
                chances -= 1
                print('Oops! Wrong guess. {} chances left.'.format(chances))

        # If all chances are used up
        if chances == 0:
            print('You lost! The word was "{}".'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
