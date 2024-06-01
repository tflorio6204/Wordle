import random

def showGuess(guess, target_word):
    result = ""
    target_word_list = list(target_word)  # Convert to list for easier manipulation
    guess_marks = [''] * len(guess)  # Placeholder for colored guess letters

    # First pass: mark correct letters (green)
    for i in range(len(guess)):
        if guess[i] == target_word[i]:
            guess_marks[i] = GREEN + guess[i] + RESET
            target_word_list[i] = None  # Remove matched letter from target_word_list

    # Second pass: mark present letters (yellow)
    for i in range(len(guess)):
        if guess_marks[i] == '':  # Only process if not already marked as green
            if guess[i] in target_word_list:
                guess_marks[i] = YELLOW + guess[i] + RESET
                target_word_list[target_word_list.index(guess[i])] = None  # Remove matched letter
            else:
                guess_marks[i] = guess[i]

    result = "".join(guess_marks)
    return "Your Guess: " + result

def checkNumOccurence(guess):
    occur_count = 0
    for char in guess:
        if char.isnumeric():
            occur_count += 1
    if occur_count > 0:
        return True
    return False
    

words_file_path = "/Users/Tommy/Python Files/words.txt"
with open(words_file_path, 'r') as file:
    words = file.read().splitlines()
target_word = random.choice(words)

print("\nWelcome to Wordle!\n")

guess_count = 0
is_won = False
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
        
user_guess = input("\nPlease guess the 5 letter word: ").lower()
while len(user_guess) != 5 or checkNumOccurence(user_guess) or user_guess not in words:
    user_guess = input("\nInvalid input or word not in list! Please guess a valid 5 letter word: ").lower()

while guess_count < 6 and is_won == False:
    if guess_count != 0:
        user_guess = input("\nPlease guess another 5 letter word: ").lower()
        while len(user_guess) != 5 or checkNumOccurence(user_guess) or user_guess not in words:
            user_guess = input("\nInvalid input or word not in list! Please guess another valid 5 letter word: ").lower()
        print(showGuess(user_guess, target_word))
        if user_guess == target_word:
            is_won = True
    else:
        print(showGuess(user_guess, target_word))
        if user_guess == target_word:
            is_won = True
    guess_count += 1

if guess_count == 6 and is_won == False:
    print("\nYou ran out of guesses! The word was", target_word + "!\n")
else:
    print("\nYou guessed", target_word, "in", guess_count, "tries!\n") 
