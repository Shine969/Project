import os
#Initialize variables
allowedTries = 6
tries = 0
guessedLetters = [] 
guessedLetter = ''
wordFound = False

#Clear console
os.system('cls')

try:
    #Input and validation
    wordToGuess = input("Enter a word to guess ヾ(⌐■_■)ノ♪ :")
    while not wordToGuess.isalpha():
        wordToGuess = input("Invalid input!:( Enter a valid word:")
    wordToGuess = list(wordToGuess.lower())
    progress = ['_' for i in range(0,len(wordToGuess))]

    #Clear Cosnsole 
    # Player 2's turn
    os.system('cls')
    print("The game is starting now!!!")

    while tries < allowedTries and not wordFound:

        #Prints Informaion that the user needs to know
        print("You have " + str(allowedTries - tries) + " tries left")
        print("Used letters:", end = " ")
        print(*guessedLetters, sep = ",")
        print("Word:", end = " ") 
        print(*progress) #print all the elements of the list in one line
        guessedLetter = str(input("Guess a letter:")).lower() #


        #Checks if input is 1 word letter
        while len(guessedLetter) != 1 or not guessedLetter.isalpha():
            print("Invalid Input!:( Enter a valid input!")
            guessedLetter = str(input("Guess a letter ヾ(⌐■_■)ノ♪:")).lower()


        #Check if the guessed letter have been guessed in the past
        if guessedLetter in guessedLetters:
            os.system('cls')
            print("###(´･ω･`)?You have already guessed this letter!###")
            continue
        else:
            guessedLetters.append(guessedLetter)

        for index,letter in enumerate(wordToGuess):
            if letter == guessedLetter:
                indixes = [i for i, x in enumerate(wordToGuess) if x == guessedLetter] #Find all the occurrences of the guessedLetter in the word
                for i in indixes:
                    progress[i] = letter #Replace found occurrences of the guessedLetter in the word with the guessedLetter
                
                wordFound = False if '_' in progress else True #If there is no _ in the progress then the user found all the missing letters
                break #if the guessedLetter was found we dont need to compare the rest of the letters
            elif index == len(wordToGuess) - 1 : #if the loop is in the last iteration and the leter is not guessed right the tries++
                tries += 1

        os.system('cls')

    if wordFound:
        print("ヾ(≧▽≦*)o You guessed the word:", end = " ")
        print(*progress, sep ="", end = "!\n")
    else:
        print("Try AGAIN!!! (┬┬﹏┬┬)", end = " "), 
        print("The word you had to guess was:", end = " ")
        print(*wordToGuess, sep = "", end = "!")

except:
	print("An exception has occured")