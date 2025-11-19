import functions #the problem with this is you will have to add 'functions.' before the functions
    
print("Welcome to Hang-Man!")
print()

user_name = input("Please enter your username: ").capitalize()

print("Welcome",user_name,"!")
print()

print("Before starting, let me explain the rules of the game:")
print("- The computer will think of a secret word")
print("- The user has to guess either a letter or the entire word")
print("- The user has five lives")
print()

#words = ["hangman", "python", "rollercoaster", "computer", "Chemistry", "Actor", "halloween", "ghost"]
easy_words = ["cat", "dog", "sun", "tree", "book", "ball", "fish", "moon", "car", "milk"]
medium_words = ["garden", "yellow", "rocket", "window", "jungle", "dragon", "pencil", "basket", "animal", "silver"]
hard_words = ["zephyr", "labyrinth", "xylophone", "chrysalis", "pharaoh", "quizzical", "oxygenate", "avalanche", "mystify", "crysanthemum"]

#Used ascii table for the Alphabet list
lowercase = [chr(i) for i in range(97, 123)] #range does not include the last value

while True:
    print("GAME MODES: ")
    print("-easy ")
    print("-medium ")
    print("-hard ")
    mode = input("Please enter the mode you want to play: ").lower()

    # each game

    lives = 5
    correctguesses = ""
    incorrectguesses = ""
    from random import choice
    
    if mode == "easy":
        word = choice(easy_words)
    
    elif mode == "medium":
        word = choice(medium_words)
    
    elif mode =="hard":
        word = choice(hard_words)
    else:
        print("Invalid input")
    
    #print(word) #don't leave this in. Mainly for testing
    
    functions.printfigures (lives)
    functions.printHidden(word, correctguesses)
    
    while lives > 0 and functions.notguessed(word, correctguesses) :
        print(f"You have {lives} lives remaining.")
        guess = input("Make a guess: ").lower()
        while guess not in lowercase:
            guess = input("Make a valid guess: ").lower()
        if guess in word:
            print()
            print("Your guess is correct :D")
            if guess not in correctguesses:
                correctguesses = correctguesses + guess
                
            else:
                print()
                print("This guess has already been made")
        else:
            print()
            print("Your guess is incorrect :(")
            if guess not in incorrectguesses:
                lives = lives - 1
                incorrectguesses = incorrectguesses + guess
                
            else:
                print("This guess has already been made")
                print("Don't wprry. We didn't count it.")
        
        functions.printfigures (lives)       
        functions.printHidden(word, correctguesses)
    
    if lives == 0:
        print("You lost the game.")
        
    else:
        print("You WON the game!")  
        
    choice = input("Do you want to end the game? (yes/no) ").lower()
    if choice == "yes":
        #break is another way to end the loop
       break 




