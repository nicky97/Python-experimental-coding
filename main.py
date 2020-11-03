import random

import classes

choice = ""
while choice != "exit":
    print("Enter 'start' to play game")
    print("Enter 'add' to add new words to your game")
    print("Enter 'exit' to exit the game")
    choice = input("Enter your choice:")
    if choice == "start":
        randomWords = list(open("wordSource.txt", "r").read().split())
        randomNumber = random.randint(0,len(randomWords)-1)
        randomWord = randomWords[randomNumber]
        Guess = classes.Phrase(randomWord)
        while True:
            Guess.showWord()
            CHAR = input("Enter a char: ")
            Guess.isPresent(CHAR)
            if Guess.isDone():
                print("You have succesfully guessed the word")
                break
    elif choice == "exit":
        print("I hope that you enjoyed the game \n HAVE A NICE DAY")

    elif choice == "add":
        while True:
            flag = True
            newWord = input("Enter a word:")
            f = open("wordSource.txt", "r")
            stringFile = f.read()
            if newWord in stringFile:
                flag = False

            f.close()
            if flag:
                af = open("wordSource.txt", "a")
                af.write("\n")
                af.write(newWord)
                af.close()
                af.close()
                print("Succesfully added a new word to the file")
            elif flag == False:
                print(f"The file already have the '{newWord}' word")
            else:
                print("Invalid word")
            choice1 = input("To exit to main menu enter exit to continue adding enter add:")
            if choice1 == "exit":
                break