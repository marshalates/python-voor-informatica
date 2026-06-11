import random


def Guess(): 
    #variables and lists, the names should be pretty clear to what they are
    words  = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier" ,"fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]
    chosenWord = random.choice(words)

    invisWord = [] #basically just the list that will show the word in a censored way (_ _ _ _ _)
    guessedLetters = []
    win = False
    turns = 5
    guess = None

    # the start text
    #shows the number of turns and shows the number of letters in the word
    print("You have " + str(turns) + " turns left.")
    print("The word contains " + str(len(chosenWord)) + " letters.")
    for letter in chosenWord:
        invisWord.append("_")
    print(''.join(invisWord)) # ''.join(invisWord) just means you print the word without the brackets and comma's

    #will keep looping until you win the game by guessing all the letters or the correct word
    while not win: 

        #takes the guess
        #if it is smaller than 1 letter or has non-letter characters, will make you guess again until everything is fine
        guess = input("Guess a letter or the full word: ").lower()
        while not len(guess) >= 1 or not guess.isalpha():
            print("That is not a valid guess, try again.")
            guess = input("Guess a letter or the full word: ")

        #if a single letter is guessed, will continue the normal way
        if len(guess) == 1 and not guess in guessedLetters:

            #if the guess is correct, shows you where it is in the word and what you still need
            if guess in chosenWord and not guess in guessedLetters:
                guessedLetters.append(guess)
                invisWord.clear()
                for letter in chosenWord:
                    if not letter in guessedLetters:
                        invisWord.append("_")
                    else: 
                        invisWord.append(letter)
                print(''.join(invisWord))

            #if the guess is not correct, take away a turn and check if you have turns left
            elif not guess in chosenWord and not guess in guessedLetters:
                guessedLetters.append(guess)
                turns -= 1
                print("That guess is incorrect.")
                if turns == 0: 
                    print("You lost, the word was " + chosenWord + ".")
                    exit()
                print("You have " + str(turns) + " turns left.")
                print(''.join(invisWord))

            #if you already guessed the letter, tells you and makes you guess again
            elif guess in guessedLetters:
                print("You have already guessed that!")

        #if a word is guessed, will check if the word is correct
        elif len(guess) > 1 and guess == chosenWord and not guess in guessedLetters:
            win = True

        #if the word is wrong, will take away a turn and check if you have turns left
        elif len(guess) > 1 and guess != chosenWord and not guess in guessedLetters:
            guessedLetters.append(guess)
            print("That was not the correct word.")
            turns -= 1
            if turns == 0: 
                print("You lost, the word was " + chosenWord + ".")
                exit()
            print("You have " + str(turns) + " turns left.")

        #if the word has been guessed before, makes you guess again
        elif guess in guessedLetters:
            print("You have already guessed that word.")

        #if you guessed all the letters, you win the game
        if not "_" in invisWord:
            win = True

    #if you won, congratulates you and stops the game  
    if win:
        print("Congrats, you guessed the word!")
        exit()

#keeps running game until it is shut down
while True:
    Guess()