import random

def hangman():
    word_list = ["python", "programming", "hangman", "computer", "game"]
    word = random.choice(word_list)
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(display_word)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        else:
            guessed_letters.append(guess)
            if guess not in word:
                attempts -= 1
                print(f"Wrong guess! {attempts} attempts left.")

        if "_" not in display_word:
            print("Congratulations! You've guessed the word.")
            break

    if "_" in display_word:
        print(f"Sorry, you've run out of attempts. The word was '{word}'.")

hangman()