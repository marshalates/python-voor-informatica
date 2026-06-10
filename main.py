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
    print("Je hebt " + str(turns) + " beurten over.")
    print("Het woord heeft " + str(len(chosenWord)) + " letters.")
    for letter in chosenWord:
        invisWord.append("_")
    print(''.join(invisWord)) # ''.join(invisWord) just means you print the word without the brackets and comma's
    
#will keep looping until you win the game by guessing all the letters or the correct word
while not win: 

    #takes the guess
    #if it is smaller than 1 letter or has non-letter characters, will make you guess again until everything is fine
    guess = input("Raad de letter of het volledige woord: ").lower()
    while not len(guess) >= 1 or not guess.isalpha():
        print("Dat is geen goede keuze, probeer nog een keer.")
        guess = input("Raad de letter of het volledige woord: ")

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
            print("Je hebt het goed geraden.")
            if turns == 0: 
                print("Je hebt verloren, je woord was " + chosenWord + ".")
                exit()
            print("Je hebt " + str(turns) + " beurten over.")
            print(''.join(invisWord))

