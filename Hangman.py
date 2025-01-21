import random

name = input("What's their name? ")
print("Welcome", name)

words = [
    "Act", "Bat", "Car", "Dog", "Egg", "Fun",
    "Acid", "Blue", "Crown", "Dive", "Evil", "Fast",
    "Alert", "Beach", "Chime", "Drift", "Echo", "Flash",
    "Bright", "Clutch", "Dance", "Fasten", "Gloomy", "Hasty",
    "Advent", "Banish", "Cuddle", "Fright", "Gentle", "Harsh",
    "Business", "Change", "Danger", "Humorous", "Intrigue", "Kinetic",
    "Abandoner", "Complexed", "Embrace", "Forgotten", "Gripping", "Harvest",
    "Adventure", "Exhausted", "Hospital", "Creative", "Freedom", "Initiative"
]

word = random.choice(words).lower()  # Ensure the word is in lowercase for comparison
guessed_letters = []  # Store guessed letters to avoid repeating guesses
j = 0  # Initialize body part count

# Inform the player of how many letters are in the word
print(f"The word has {len(word)} letters.")

# Game loop
while j < 10:
    guess = input("What's your guess (a letter): ").lower()  # Get user input and convert to lowercase
    
    # Check if the guess is a valid single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter a single letter.")
        continue  # Skip the rest of the loop and ask for input again
    
    # Avoid repeating guesses
    if guess in guessed_letters:
        print("You've already guessed that letter!")
        continue

    guessed_letters.append(guess)  # Add the guess to the guessed letters list
    
    if guess in word:
        print(f"{guess} is in the word.")
    else:
        print("Incorrect, adding body part.")
        j += 1
        print(f"{j} body part(s) added.")

    # Check for win or loss
    if j == 10:
        print("You lose :(")
        final_guess = input("You've lost! Can you guess the word? ").lower()
        if final_guess == word:
            print("Congrats! You guessed the word correctly!")
        else:
            print(f"The word was: {word}")
        break
    elif all(letter in guessed_letters for letter in word):
        print("CONGRATS!!! You win!!! :D")
        print(f"The word was: {word}")
        break
