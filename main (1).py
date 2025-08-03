'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import random

# Predefined list of words
word_list = ['apple', 'robot', 'candy', 'pizza', 'chair']
secret_word = random.choice(word_list)

# Game variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Display setup
display_word = ['_'] * len(secret_word)

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# Game loop
while wrong_guesses < max_wrong_guesses and '_' in display_word:
    print("\nWord: " + ' '.join(display_word))
    print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")
    print("Guessed letters:", ' '.join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
        for index, letter in enumerate(secret_word):
            if letter == guess:
                display_word[index] = guess
    else:
        print("❌ Wrong guess.")
        wrong_guesses += 1

# Game result
if '_' not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 Game Over! The word was:", secret_word)
