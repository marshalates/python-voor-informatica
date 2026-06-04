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
