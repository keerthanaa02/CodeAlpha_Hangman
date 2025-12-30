import random

# Step 1: Word list
words = ["apple", "banana", "orange", "grapes", "mango"]
word = random.choice(words)
display = ["_"] * len(word)
guessed = []
wrong_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")
print("Guess the word:", " ".join(display))

# Step 3: Game loop
while wrong_guesses < max_guesses and "_" in display:
    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                display[i] = guess
        print("Correct:", " ".join(display))
    else:
        wrong_guesses += 1
        print(f"Wrong guess! Attempts left: {max_guesses - wrong_guesses}")

# Step 4: End conditions
if "_" not in display:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game over! The word was:", word)