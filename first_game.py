# guess the random word:-
import random

def get_random_word():
    words = ["python", "java", "ruby", "javascript", "html", "css"]
    return random.choice(words)

def display_hint(word, guess):
    hint = ['_'] * len(word)
    for i in range(len(word)):
        if i < len(guess) and guess[i] == word[i]:
            hint[i] = word[i]
    return ''.join(hint)

def main():
    print("Welcome to 'Guess the Word'!")
    word = get_random_word()
    attempts = 0
    max_attempts = 6
    
    print(f"Guess the word! It's a {len(word)}-letter word.")

    while attempts < max_attempts:
        guess = input("Enter your guess: ").lower()
        
        if len(guess) != len(word):
            print(f"Please enter a {len(word)}-letter word.")
            continue
        
        if guess == word:
            print("Congratulations! You've guessed the word!")
            break
        
        hint = display_hint(word, guess)
        print(f"Hint: {hint}")
        
        attempts += 1
        print(f"Attempts left: {max_attempts - attempts}")
        
    if guess != word:
        print(f"Sorry, you've used all your attempts. The word was '{word}'.")

if __name__ == "__main__":
    main()