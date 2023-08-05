import random

# List of riddles and their corresponding answers
riddles = [
    ("How many climate change skeptics does it take to change a lightbulb?", "None. It's too early to say if the lightbulb needs changing"),
    ("If you live in an igloo, what's the worst thing about global warming?", "Melting ice"),
    ("If it's zero degrees outside today and it's going to be twice as cold tomorrow, how cold is it going to be?", "Zero degrees. Two times zero is still zero."),
    ("This type of place has a lack of rain
So it is a dry and arid land
The most famous ones the Sahara
Which is covered in a lot of sand", "Arid/Desert")
    # Add more riddles here
]

def select_random_riddle():
    return random.choice(riddles)

def play_riddle_game():
    print("Welcome to the Riddle Game!")
    riddle, correct_answer = select_random_riddle()
    print("Here's your riddle:")
    print(riddle)

     guess = input("Your guess: ").strip().lower()

    if guess == correct_answer:
        print("Congratulations! You guessed correctly.")
    else:
        print(f"Sorry, that's incorrect. The correct answer is: {correct_answer}")

if __name__ == "__main__":
    play_riddle_game()
