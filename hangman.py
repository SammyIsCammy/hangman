import random

#list_of_words = ["REPRESENT", "EXHAUST", "THRUST", "BLAME", "INVEST", "REINFORCE", "VIEW",
#"TRANSFORM", "EXECUTE", "RAIN"]

list_of_words = ["rain"]

# Selects a random word from the list of words and separates the characters to form a list. EXAMPLE: ["R", "A", "I", "N"]
selected_word = list(random.choice(list_of_words))
print(selected_word)

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

# Number of underscrolls to appear that will disappear upon every correct character guess
blanks = [] 
for blank in range(len(selected_word)):
    blanks.append("_")
print(*blanks)


while blanks != selected_word:
    guess = input("Guess a letter: ")
    if guess.isalpha() == False:
        print("You cannot enter a number, symbol, or space!")


    for i in range(len(selected_word)):
        if guess == selected_word[i]:
            blanks[i] = guess

    print(*blanks)


