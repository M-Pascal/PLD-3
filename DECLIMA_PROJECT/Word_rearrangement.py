import random

def load_words(filename):
    with open(filename, 'r') as file:
        return [word.strip() for word in file.readlines()]

def pick_random_word(words_list):
    return random.choice(words_list)

def rearrange_letters(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

def is_word_valid(guess, correct_word):
    return guess.lower() == correct_word.lower()

def game():
    words_to_guess = load_words("words.txt")
    definitions = {}
    with open("definitions.txt", 'r') as file:
        for line in file:
            word, definition = line.strip().split(':', 1)
            definitions[word] = definition.strip()

    print("Welcome to the Word Rearrangement Game!")

    while True:
        word_to_guess = pick_random_word(words_to_guess)
        shuffled_word = rearrange_letters(word_to_guess)

        print("\nYou have 3 attempts to rearrange the letters and find the correct word related to climate change.")
        print(f"Rearrange the letters!: {shuffled_word}")

        for attempt in range(1, 4):
            guess = input(f"Attempt {attempt}: ").strip()

            if is_word_valid(guess, word_to_guess):
                print("Congratulations! You found the correct word!")
                print(f"The word '{word_to_guess}' means: {definitions[word_to_guess]}")
                break
            else:
                print("Incorrect guess. Try again!")

        else:
            print(f"\nYou've used all your attempts. The correct word was '{word_to_guess}'.")
            print(f"The word '{word_to_guess}' means: {definitions[word_to_guess]}")

        choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    game()
