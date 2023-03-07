import random
import os

list_of_words = ["rain"]

# Selects a random word from the list of words and separates the characters to form a list. EXAMPLE: ["R", "A", "I", "N"]
selected_word = list(random.choice(list_of_words))


# Number of underscrolls to appear that will disappear upon every correct character guess
blanks = [] 
for blank in range(len(selected_word)):
    blanks.append("_")


# Function that prints the HANGMAN banner and prints the amount of letters to fill in
def banner():
    print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
                   """)

    print(*blanks)


# Function that runs if you lose
def lose():
    os.system("cls")
    print("YOU HUNG YOUR MAN!")
    print("""
                _______
                |/      |
                |      (_)
                |      \|/
                |       |
                |      / \\
                |
            ____|___""")
    

# Function that runs if you win
def win():
    os.system("cls")
    print("""             
            OOOOOOOOOOO
         OOOOOOOOOOOOOOOOOOO
      OOOOOO  OOOOOOOOO  OOOOOO
    OOOOOO      OOOOO      OOOOOO
  OOOOOOOO  #   OOOOO  #   OOOOOOOO
 OOOOOOOOOO    OOOOOOO    OOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOO  OOOOOOOOOOOOOOOOOOOOOOOOO  OOOO
 OOOO  OOOOOOOOOOOOOOOOOOOOOOO  OOOO
  OOOO   OOOOOOOOOOOOOOOOOOOO  OOOO
    OOOOO   OOOOOOOOOOOOOOO   OOOO
      OOOOOO   OOOOOOOOO   OOOOOO
         OOOOOO         OOOOOO
             OOOOOOOOOOOO\n""")
    print("CONGRATS!!! YOU WIN!!!")


counter = len(selected_word)


while blanks != selected_word and counter > 0:
    banner()
    guess = input("Guess a letter: ")
    if guess.isalpha() == False:
        print("You cannot enter a number, symbol, or space!")


    for i in range(len(selected_word)):
        if guess == selected_word[i]:
            blanks[i] = guess


    if guess in selected_word or guess.isalpha() == False:
        counter = counter
    elif not guess in selected_word:
        counter -= 1

    print(*blanks)

    if counter == 0:
        lose()

    if blanks == selected_word:
        win()
