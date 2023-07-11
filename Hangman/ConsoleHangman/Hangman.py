import random


def opening_text():  ## --> O(1)
    # prints the opening screen with instructions etc
    
    sapce = " " * 37
    print(sapce+"   ---------------------------------------------------------------\n",
          sapce+" |                            ____                               |\n",
          sapce+" |      |     |   /\   |\  | |          |\  /|   /\   |\  |      |\n",
          sapce+" |      |-----|  /__\  | \ | |  __      | \/ |  /__\  | \ |      |\n",
          sapce+" |      |     | /    \ |  \| |____|     |    | /    \ |  \|      |\n",
          sapce+"  ---------------------------------------------------------------\n",
        
          sapce + "   |Rules:                                                     |\n",
          sapce + "   | #1. You will be guessing a word                           |\n",
          sapce + "   | #2. length of word is based on the difficulty you choose. |\n",
          sapce + "   | #3. You have 6 lives.                                     |\n",
          sapce + "   | #4. Enter ! to quit.                                      |\n",
          sapce + "   | #5. You have 3 life lines!                                |\n",
          sapce + "   |                                                           |\n",
          sapce + "   |  Enter the appropirate number to use a life line:         |\n",
          sapce + "   |     1 ->Get a random correct letter                       |\n",
          sapce + "   |     2 ->Eliminate a useless letter                        |\n",
          sapce + "   |     3 ->You may gain a life or lose a life, its a gamble! |\n",
          sapce + "   |" + " _" * 29 + " |\n",
        )


def choose_diff(): ## --> O(n)
    # returns the name of the text file, according to the difficulty the user chooses

    print("\n", " " * 38, "Choose a difficulty:")
    print(" " * 40, "  1.Easy  2.Medium  3.Hard  4.Nightmare  5.Random")

    diff = input(" " * 43)
    while diff not in ["1","2","3","4","5"]:
        print(" " * 42, "Please choose a number from [1,2,3,4,5]")
        diff = input(" " * 43)
    
    textfile = ""

    if diff == "1":
        textfile = "words len 00 - 05.txt"
    if diff == "2":
        textfile = "words len 06 - 10.txt"
    if diff == "3":
        textfile = "words len 11 - 15.txt"
    if diff == "4":
        textfile = "words len 16 - 22.txt"
    if diff == "5":
        textfile = "all_words.txt"

    return textfile


def draw_gallows(stage=0, life=0, hints=[]):  ## --> O(1)
    # Function is used to print the body of the hangman. By entering the stage number(i.e tried made) of the game, 
    # the body will be, printed accordingly. >6 or <0 = prints gallows 1 = head. 2 = chest. 3 = right arm. 4 = left 
    # arm. 5 = right leg. 6 = left leg 

    # The strings for each appendage of the hangman
    head = " " * 12 + "O"
    chest = " " * 12 + "|"
    right_arm = " " * 12 + "|" + "/"
    both_arm = " " * 11 + "\\" + "|" + "/"
    right_leg = " " * 13 + "\\"
    both_leg = " " * 11 + "/" + " \\"

    appendage1, appendage2, appendage3, appendage4 = "", "", "", ""  # Initiallized to empty string. Only the gallow will be initally printed.

    # Adds each appendage to the hangman according to the stage number.
    if stage == 6:
        appendage1 = head

    elif stage == 5:
        appendage1 = head
        appendage2 = chest
        appendage3 = chest

    elif stage == 4:
        appendage1 = head
        appendage2 = right_arm
        appendage3 = chest

    elif stage == 3:
        appendage1 = head
        appendage2 = both_arm
        appendage3 = chest

    elif stage == 2:
        appendage1 = head
        appendage2 = both_arm
        appendage3 = chest
        appendage4 = right_leg

    elif stage == 1:
        appendage1 = head
        appendage2 = both_arm
        appendage3 = chest
        appendage4 = both_leg

    print("  " + "-" * 13 + "|" + " Tries:", life, " -|- Hints: ", [int(avail_hints) for avail_hints in hints])
    print("  |" + " " * 11 + "_" + "|" + "_")
    print("  |" + appendage1)
    print("  |" + appendage2)
    print("  |" + appendage3)
    print("  |" + appendage4)
    print("  |")
    print("-" * 13)


def alphabets(letter="", abc=[], abc_used=[], print_check=False):  ## --> O(n)
    # Prints list of available and used alphabets. Adds them to their respective list
    letter = letter.upper()

    for i in range(0,len(abc) - 1): # removes letter from alphabets and adds the input letter to the list of used letters 
        if abc[i] == letter:
            abc_used.append(letter)
            del abc[i]

    if letter == "Z":
        abc_used.append(letter)
        abc.remove(letter)

    if print_check is True: # for if printing the lists is needed
        for ii in abc: # prints list of available letters
            print(ii, end=" ")

        print(" -|- Used --> [", end="")

        for iii in abc_used: # prints list of used alphabets
            print(iii, end=" ")

        print("]", end="")


def word_blanks(word):  ## --> O(n)
    # Splits the word letter by letter into a list and creates a list with blanks equal to the word
    word = list(word.upper())

    for i in range(0,len(word) - 1): # splits the word into seperate lines in case a phrase is used
        if word[i] == " ":
            word[i] = "\n"

    blanks = []

    for i in range(len(word)): # prints a blank for every unguessed letter
        blanks.append("_")

        if word[i] == "\n":
            blanks[i] = "\n"

    return word, blanks


def letter_check(letter, word, blanks):  ## --> O(n)
    # If the letter is in the word, it repalces a blank with the letter
    letter = letter.upper()

    for i in range(len(word)): # if the input letter is in the word, a blank is replaced with that correct letter in its place
        if letter == word[i]:
            blanks[i] = letter


def guess_validity(input_letter, abc_used, hint_list):  ## --> O(n)
    # To validate the input. Only unused alphabets, hint nums and exit(!) is accepted.

    if input_letter == "!": # If the user wants to quit
        return input_letter

    if input_letter in hint_list: # If the input letter is a hint num
        return input_letter


    while (input_letter in ["1", "2", "3"] and input_letter not in hint_list) or \
        (input_letter.isalpha() is False) or \
        (input_letter in abc_used) or \
        (len(input_letter) > 1): 
        # If the user enters anything but an unsed alphabet or hint num. Stays in loop until correct input is given

        if input_letter in ["1", "2", "3"] and input_letter not in hint_list: # if input hint num is already used
            input_letter = input("You have already used this Lifeline. \nEnter a new guess: ").upper()
            if input_letter in hint_list:
                return input_letter.upper()

        if input_letter.isalpha() is False and input_letter not in ["1","2","3"]: # if input isnt an alphabet
            input_letter = input("Please enter an alphabet: ").upper()

        if input_letter in abc_used: # if input is already used
            input_letter = input("This is used. Make a new guess: ").upper()

        if len(input_letter) > 1: # if input is more then a single letter
            input_letter = input("Enter a single letter: ").upper()

        if input_letter in ["1", "2", "3"] and input_letter in hint_list:
            return input_letter.upper()


    return input_letter


def win_check(blanks):  ## --> O(n)
    # keeps track of whether the user has won or now. Returns True if user has won the game

    for i in blanks: # if there are no blanks left, then the user has guesses all the letters and has won
        if i == "_":
            return False
    return True


def get_random_word(): ## --> O(n)
    # Gets a random word from the chosen text file
    
    file_name = choose_diff()
    all_words = open("text_files\\" + file_name).read().splitlines() # Opens the text file and gets a list of all the words in the file
    
    return random.choice(all_words) # Gets a random word from the list


def hints(hint_num=0, letters=[], blanks=[], avail_letters=[], used_letters=[]):  ## --> O(n)
    # Handles the work for each the 3 hints


    if hint_num == "1":  # 1 ->get a random correct letter for free

        rand_i = random.randint(0, len(blanks) - 1) # gets a random index
        while (blanks[rand_i] != "_"): # Finds an index in the word that isnt a blank. i.e find a letter in the word that hasnt been guessed yet
            rand_i = random.randint(0, len(blanks) - 1)

        print("You are using hint 1")
        print("You receive the letter, ", letters[rand_i], " for free !")
        letter_check(letters[rand_i], letters, blanks) # repalces a blannk with the random letter found earlier
        return letters[rand_i]

    if hint_num == "2":  # 2 ->eliminate a useless letter for free

        rand_i = random.randint(0, len(avail_letters) - 1) # gets a random index
        while (avail_letters[rand_i] in letters or avail_letters[rand_i] in used_letters): # finds a letter that hasnt been used and is not in the word
            rand_i = random.randint(0, len(avail_letters) - 1)

        print("using hint 2")
        print(avail_letters[rand_i], " has been removed from usage without losing life!")
        return avail_letters[rand_i]

    if hint_num == "3":  # 3 ->80% chance to gain back a life. 20% chance to lose a life 
        luck = random.randint(1, 10)
        if luck <= 8:
            print("Lucky dog! You just gained a life")
            return True
        if luck >= 9:
            print("You lost a life. Dont gamble kids")
            return False


def hangman(word):
    # Does all the work for the game. 
    
    chances = 7
    input_guess = ""

    abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"] # List of available letters
    abc_struck = [] # List of used letter

    word_list_initialize = word_blanks(word) # Initalises tuple containing a list for the word and list for blanks
    letter_list = word_list_initialize[0] # the word is stored as a list
    blanks_list = word_list_initialize[1] # list of blank spaces
    life_lines = ["1", "2", "3"]

    while chances != 1: # Loops until user runs out of chances or win_check() returns True
        print(" " * 42, "*" * 48)

        [print(blanks, end=" ") for blanks in blanks_list] # Prints blank spaces according to the word

        print("\n")
        draw_gallows(chances, chances - 1, life_lines) # Prints gallows according to the chances left
        alphabets(input_guess, abc, abc_struck, True) # Prints list of available and used alphabets 
        print("\n")

        input_guess = guess_validity(input("Enter your guess: ").upper(), abc_struck, life_lines) # Validates the input
         
        if input_guess == "!":  # Quit game
            print("You quit the game. Word was --> ", word.title())
            break
        
        # Handles all work regarding Hint inputs
        if input_guess == "1" and input_guess in life_lines:
            
            life_lines.remove("1")
            input_guess = hints("1", letter_list, blanks_list, abc, abc_struck) # Gives a random letter from the word
            alphabets(input_guess, abc, abc_struck, False) # Updates the available and used alphabets
            
            if win_check(blanks_list) is True:
                break

            continue

        if input_guess == "2" and input_guess in life_lines:
            life_lines.remove("2")
            remove_letter = hints("2", letter_list, blanks_list, abc, abc_struck) # Gets a random useless letter

            alphabets(remove_letter, abc, abc_struck, False) # Removes that letter from play
            
            continue

        if input_guess == "3" and input_guess in life_lines:
            life_lines.remove("3")
            lucky = hints("3") # Returns True if user +1 chacnce. False if -1 chance
            
            if lucky is True:
                chances += 1
            else:
                chances -= 1
            continue


        if input_guess in letter_list: # If the user guesses a correct letter
            print("\nGood guess.", input_guess, "is in the word.")
            letter_check(input_guess, letter_list, blanks_list)

            if win_check(blanks_list) is True:
                break

        else: # If user is incorrect
            print("\nBad guess.", input_guess, "is not in the word. Try again.")
            chances -= 1

        print(" " * 42, "*" * 48)

    # Prints whether the user has won or lost 
    if chances == 1:
        draw_gallows(1, 0, life_lines)
        print("\nYou lost. The word was: ", word.title())
    elif input_guess != "!":
        print("\nYou won. The word was: ", word.title())


if __name__ == "__main__":

    opening_text()
    end_game = 0
    while end_game != "1":
        
        word = get_random_word()
        hangman(word)
        
        print("-" * 50)
        end_game = input("\nPress 1 to end. \nPress any key to restart\n")
        print("\n" * 30)