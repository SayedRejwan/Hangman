import random

def choose_word(category=None):
    """Select a word based on the chosen category or randomly."""
    categories = {
        'Animals': ['tiger', 'elephant', 'giraffe', 'kangaroo', 'penguin'],
        'Sports': ['soccer', 'cricket', 'tennis', 'hockey', 'basketball'],
        'Countries': ['canada', 'brazil', 'japan', 'germany', 'india']
    }
    
    if category and category in categories:
        return random.choice(categories[category])
    else:
        all_words = [word for word_list in categories.values() for word in word_list]
        return random.choice(all_words)

def display_word(word, guessed_letters):
    """Display the current state of the word with underscores for unguessed letters."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def show_hangman(attempts_left):
    """Display hangman ASCII art based on attempts left."""
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
                -----
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /     |
                -----
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
                |
                -----
        """,
        """
           -----
           |   |
           O   |
          /|    |
                |
                -----
        """,
        """
           -----
           |   |
           O   |
           |    |
                |
                -----
        """,
        """
           -----
           |   |
           O   |
                |
                |
                -----
        """,
        """
           -----
           |   |
                |
                |
                |
                -----
        """
    ]
    print(stages[6 - attempts_left])

def hangman():
    print("Welcome to Hangman!")

    # Choose category
    print("Choose a category:")
    print("1. Animals")
    print("2. Sports")
    print("3. Countries")
    category = input("Enter the number of your choice (or press Enter for random): ")
    
    category_map = {'1': 'Animals', '2': 'Sports', '3': 'Countries'}
    chosen_category = category_map.get(category, None)

    # Select a random word
    word = choose_word(chosen_category)
    guessed_letters = set()
    attempts_left = 6
    hint_used = False

    while attempts_left > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        show_hangman(attempts_left)
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")

        if not hint_used:
            use_hint = input("Would you like a hint? (yes/no): ").lower()
            if use_hint == 'yes':
                print(f"Hint: The word is related to {chosen_category if chosen_category else 'a random topic'}.")
                hint_used = True

        # Get user's guess
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            # Check if the user has guessed all the letters
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            print("Wrong guess.")
            attempts_left -= 1

    if attempts_left == 0:
        show_hangman(attempts_left)
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
