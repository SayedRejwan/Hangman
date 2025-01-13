import tkinter as tk
from tkinter import messagebox
import random

# Adaptive Word Lists
words_by_difficulty = {
    'Easy': ['cat', 'dog', 'fish', 'bird', 'cow'],
    'Medium': ['python', 'zebra', 'guitar', 'rocket', 'planet'],
    'Hard': ['microscope', 'xylophone', 'parliament', 'dynamite', 'philosophy']
}

# Themed Hangman (Pirate Theme)
pirate_hangman = [
    "⚓ Ship: Fully Afloat! 🌊",
    "⚓ A wave hits! 🌊",
    "⚓ The mast breaks! ⛵",
    "⚓ The sails are torn! 🌪️",
    "⚓ Water is leaking in! 💦",
    "⚓ The ship is sinking! 🚢",
    "⚓ Shipwrecked! 🏝️"
]


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Themed Hangman")
        self.difficulty = tk.StringVar(value="Easy")
        self.word = ""
        self.guessed_letters = set()
        self.attempts_left = 6

        # GUI Setup
        self.setup_gui()

    def setup_gui(self):
        # Title
        tk.Label(self.root, text="Welcome to Themed Hangman!", font=("Helvetica", 16)).pack(pady=10)

        # Difficulty Selection
        tk.Label(self.root, text="Select Difficulty:").pack()
        tk.Radiobutton(self.root, text="Easy", variable=self.difficulty, value="Easy").pack()
        tk.Radiobutton(self.root, text="Medium", variable=self.difficulty, value="Medium").pack()
        tk.Radiobutton(self.root, text="Hard", variable=self.difficulty, value="Hard").pack()

        # Start Button
        tk.Button(self.root, text="Start Game", command=self.start_game).pack(pady=10)

        # Game Display
        self.word_label = tk.Label(self.root, text="", font=("Courier", 18), fg="blue")
        self.word_label.pack(pady=10)

        self.hangman_label = tk.Label(self.root, text=pirate_hangman[0], font=("Helvetica", 14), fg="red")
        self.hangman_label.pack(pady=10)

        self.guess_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.guess_entry.pack(pady=5)
        self.guess_entry.bind("<Return>", lambda _: self.make_guess())

        tk.Button(self.root, text="Submit Guess", command=self.make_guess).pack(pady=5)

        # Remaining Attempts
        self.attempts_label = tk.Label(self.root, text=f"Attempts Left: {self.attempts_left}", font=("Helvetica", 12))
        self.attempts_label.pack()

    def start_game(self):
        # Reset game state
        self.word = random.choice(words_by_difficulty[self.difficulty.get()])
        self.guessed_letters = set()
        self.attempts_left = 6

        # Update GUI
        self.word_label.config(text=self.get_display_word())
        self.hangman_label.config(text=pirate_hangman[0])
        self.attempts_label.config(text=f"Attempts Left: {self.attempts_left}")

        # Clear input field
        self.guess_entry.delete(0, tk.END)

    def get_display_word(self):
        """Return the word with guessed letters visible."""
        return ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])

    def make_guess(self):
        # Get user input
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", f"You already guessed '{guess}'.")
            return

        # Process guess
        self.guessed_letters.add(guess)
        if guess in self.word:
            self.word_label.config(text=self.get_display_word())
            if all(letter in self.guessed_letters for letter in self.word):
                messagebox.showinfo("You Win!", f"Congratulations! You guessed the word: {self.word}")
                self.start_game()
        else:
            self.attempts_left -= 1
            self.hangman_label.config(text=pirate_hangman[6 - self.attempts_left])
            self.attempts_label.config(text=f"Attempts Left: {self.attempts_left}")
            if self.attempts_left == 0:
                messagebox.showerror("Game Over", f"Out of attempts! The word was: {self.word}")
                self.start_game()


if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
