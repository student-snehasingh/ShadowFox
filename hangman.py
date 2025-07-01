import random

# Hangman stages
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
     ===''']

# Word list with hints
WORDS_WITH_HINTS = [
    ("python", "A popular programming language"),
    ("giraffe", "A tall African animal with a long neck"),
    ("astronaut", "Travels to space"),
    ("umbrella", "Protects you from rain"),
    ("pyramid", "A triangular ancient Egyptian structure"),
    ("island", "Land surrounded by water"),
    ("volcano", "Mountain that can erupt with lava"),
    ("oxygen", "Essential gas we breathe"),
    ("violin", "A string instrument you play with a bow"),
    ("jupiter", "The largest planet in the solar system")
]

def choose_word():
    return random.choice(WORDS_WITH_HINTS)

def display_progress(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_hangman():
    word, hint = choose_word()
    word = word.lower()
    guessed_letters = set()
    attempts = 0
    max_attempts = len(HANGMAN_PICS) - 1

    print("Welcome to Hangman!")
    print(f"Hint: {hint}")

    while attempts < max_attempts:
        print(HANGMAN_PICS[attempts])
        print("\nWord: ", display_progress(word, guessed_letters))
        print(f"Used letters: {' '.join(sorted(guessed_letters))}")
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠ Enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("❗ You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Wrong!")
            attempts += 1

        if all(letter in guessed_letters for letter in word):
            print("\n Congratulations! You guessed the word:", word)
            break
    else:
        print(HANGMAN_PICS[-1])
        print("\n Game Over! The word was:", word)

if __name__ == "__main__":
    play_hangman()