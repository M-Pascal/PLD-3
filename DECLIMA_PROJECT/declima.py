#Display instructions
def display_instructions():
    print("Welcome to DECLIMA!")
    print("DECLIMA is a game where you can have fun while learning more about climate change.")
    print("You can choose between two games :")
    print("1. Word Game: Rearrange letters to find a word related to climate change.")
    print("2. Riddle Game: Answer tricky questions related to climate change.")
    print()

def main():
    display_instructions()
    choice = input("If you want to play the Word Game, press 1. If you want to play the Riddle Game, press 2: ")

    if choice == '1':
        import Word_rearrangement
        Word_rearrangement.game()
    elif choice == '2':
        import riddle
        riddle.start_game()
    else:
        print("Incorrect input. Please choose either 1 or 2.")

if __name__ == '__main__':
    main()
