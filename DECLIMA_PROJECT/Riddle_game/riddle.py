import random


def main():
    display_instructions()
    riddles = select_riddle()
    play_riddle_game(riddles)


#Displays the instructions
def display_instructions():
    print("Welcome to Declima riddle game!")
    print("Instructions:")
    print("You'll be presented with riddles related to climate change.")
    print("You have 3 attempts to guess each riddle correctly.")
    print("Let's get started!")
    print("PS: Your answers should always be in lowercase.")


#Select a random riddle in the list
def select_riddle():
    riddles = [
        {"question" : "I am essential for life, but excessive amounts are causing global warming. What am I?",
         "answer" : "carbon dioxide"},
         {"question" : "I am melting rapidly due to rising global temperatures. What am I?",
          "answer" : "glacier"},
        {"question" : "I am a gas that's helpful to plants, but I cannot be bought at a gas station. What am I?",
         "answer" : "carbon dioxide"}
    ]
    return riddles  


#start playing
def play_riddle_game(riddles):
    score = 0 

#The for loop so it ends when all riddles have been used
    for riddle in riddles:
        lives_left = 3

        print("\nRiddle: " + riddle["question"])
        while lives_left > 0:
            user_guess = input("Your Answer ({} lives left): ".format(lives_left)).lower()
# Verify user guess, and remove one life if the user fail.            
            if user_guess == riddle["answer"]:
                print("Congratulations! That's the correct answer!")
                score += 1
                break
            else:
                lives_left -= 1
                if lives_left > 0:
                    print("Incorrect answer. Try again!")
                else:
                    print("GAME OVER! You've used all your lives. The correct answer was: '{}'.".format(riddle["answer"]))

    print("\nThank you for playing! Your final score: {} out of {} riddles.".format(score, len(riddles)))

        
        


if __name__ == '__main__':
    main()
