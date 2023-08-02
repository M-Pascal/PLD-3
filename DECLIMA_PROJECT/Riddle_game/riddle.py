import random


def main():
    display_instructions()
    play_riddle_game()



#Displays the instructions
def display_instructions():
    print("Welcome to Declima riddle game!")
    print("Instructions:")
    print("You'll be presented with riddles related to climate change.")
    print("You have 3 attempts to guess each riddle correctly.")
    print("Let's get started!")
    print("PS: Your answers should always be in lowercase.")


#Select a random riddle in the list
def select_random_riddle():
    riddles = [
        {"question" : "I am essential for life, but excessive amounts are causing global warming. What am I?",
         "answer" : "carbon dioxide"},
         {"question" : "I am melting rapidly due to rising global temperatures. What am I?",
          "answer" : "glacier"},
        {"question" : "I am a gas that's helpful to plants, but I cannot be bought at a gas station. What am I?",
         "answer" : "carbon dioxide"}
    ]
    return random.choice(riddles)


#start playing
def play_riddle_game(riddles):
    score = 0 
   
    for i in len(riddles):
        riddle = select_random_riddle()
        lives_left = 3




if __name__ == '__main__':
    main()