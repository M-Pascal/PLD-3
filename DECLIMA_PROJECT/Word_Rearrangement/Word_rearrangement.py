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

def game():
    words_to_guess = load_words("words.txt")
    definitions = {}
    with open("definitions.txt", 'r') as file:
        for line in file:
            word, definition = line.strip().split(':', 1)
            definitions[word] = definition.strip()

    print("Welcome to the Word Rearrangement Game!")
    print("You have 3 attempts to rearrange the letters and find the correct word related to climate change.\n")

    for _ in range(3):
        word_to_guess = pick_random_word(words_to_guess)
        shuffled_word = rearrange_letters(word_to_guess)

        print(f"Rearrange the letters: {shuffled_word}")
        guess = input("Your guess: ").strip().lower()

        if guess == word_to_guess:
            print("Congratulations! You found the correct word!")
            print(f"The word '{word_to_guess}' means: {definitions[word_to_guess]}")
            return

        print("Incorrect guess. Try again!")

    print(f"\nYou've used all your attempts. The correct word was '{word_to_guess}'.")
    print(f"The word '{word_to_guess}' means: {definitions[word_to_guess]}")

if __name__ == "__main__":
    game()
