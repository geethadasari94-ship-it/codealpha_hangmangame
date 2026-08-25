import streamlit as st
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


# Start a new game
def new_game():
    st.session_state.word = random.choice(WORDS)
    st.session_state.guessed_letters = set()
    st.session_state.incorrect_guesses = 0
    st.session_state.game_over = False


# Initialize game
if "word" not in st.session_state:
    new_game()


# Page title
st.title("🎯 Hangman Game")

st.write("Guess the word one letter at a time!")
st.write(f"You have {MAX_INCORRECT_GUESSES} incorrect guesses.")


# Display word
display_word = ""

for letter in st.session_state.word:
    if letter in st.session_state.guessed_letters:
        display_word += letter + " "
    else:
        display_word += "_ "

st.subheader(display_word)


# Show incorrect guesses
st.write(
    f"❌ Incorrect guesses: "
    f"{st.session_state.incorrect_guesses} / {MAX_INCORRECT_GUESSES}"
)


# Show guessed letters
if st.session_state.guessed_letters:
    st.write(
        "🔤 Guessed letters:",
        ", ".join(sorted(st.session_state.guessed_letters))
    )


# Check win
if all(
    letter in st.session_state.guessed_letters
    for letter in st.session_state.word
):
    st.success("🎉 Congratulations! You guessed the word!")
    st.write("The word was:", st.session_state.word)
    st.session_state.game_over = True


# Check game over
if st.session_state.incorrect_guesses >= MAX_INCORRECT_GUESSES:
    st.error("💀 GAME OVER!")
    st.write("The correct word was:", st.session_state.word)
    st.session_state.game_over = True


# Guess input
if not st.session_state.game_over:

    guess = st.text_input(
        "Enter a letter:",
        max_chars=1
    )

    if st.button("Guess"):

        if not guess:
            st.warning("Please enter a letter.")

        elif not guess.isalpha():
            st.warning("Please enter an alphabet letter.")

        elif guess.lower() in st.session_state.guessed_letters:
            st.warning("You already guessed that letter.")

        else:
            guess = guess.lower()

            st.session_state.guessed_letters.add(guess)

            if guess in st.session_state.word:
                st.success("✅ Correct guess!")

            else:
                st.session_state.incorrect_guesses += 1
                st.error("❌ Wrong guess!")

            st.rerun()


# New game button
if st.button("🔄 Play Again"):
    new_game()
    st.rerun()