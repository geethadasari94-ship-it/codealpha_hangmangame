import random

# Predefined words
WORDS = [
    "python",
    "computer",
    "program",
    "developer",
    "keyboard"
]

MAX_INCORRECT_GUESSES = 6


def display_word(word, guessed_letters):
    """Display guessed and unguessed letters."""
    result = []

    for letter in word:
        if letter in guessed_letters:
            result.append(letter)
        else:
            result.append("_")

    return " ".join(result)


def play_game():
    """Run one Hangman game."""

    word = random.choice(WORDS)
    guessed_letters = set()
    incorrect_guesses = 0

    print("\n" + "=" * 40)
    print("           HANGMAN GAME")
    print("=" * 40)
    print("Guess the word one letter at a time.")
    print("You have 6 incorrect guesses.")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:

        print("\nWord:", display_word(word, guessed_letters))

        # Check if player won
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! 🎉")
            print("You guessed the word:", word)
            return

        print(
            "Incorrect guesses:",
            incorrect_guesses,
            "/",
            MAX_INCORRECT_GUESSES
        )

        if guessed_letters:
            print(
                "Guessed letters:",
                " ".join(sorted(guessed_letters))
            )

        guess = input("Enter a letter: ").strip().lower()

        # Check input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabet letter.")
            continue

        # Check repeated letter
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # Save guessed letter
        guessed_letters.add(guess)

        # Check whether guess is correct
        if guess in word:
            print("Correct guess! ✅")
        else:
            incorrect_guesses += 1
            print("Wrong guess! ❌")

    # Game over
    print("\n" + "=" * 40)
    print("             GAME OVER")
    print("=" * 40)
    print("The correct word was:", word)


def main():
    """Start the Hangman game."""

    while True:

        play_game()

        choice = input(
            "\nDo you want to play again? (y/n): "
        ).strip().lower()

        if choice != "y":
            print("\nThank you for playing Hangman!")
            break


if __name__ == "__main__":
    main()