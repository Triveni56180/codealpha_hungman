import random

# List of words
words = ["python", "code", "alpha", "internship", "hangman"]
word = random.choice(words)  # Randomly pick a word
guessed = "_" * len(word)    # Hide the word with underscores
guessed = list(guessed)
attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman!")
print("Guess the word:", " ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"❌ Wrong! Attempts left: {attempts}")

    print("Word:", " ".join(guessed))

if "_" not in guessed:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("😢 Game Over! The word was:", word)