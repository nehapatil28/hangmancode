import random
"create the function for to play hangman"
def hangman():

    "crate list of world"
    list_of_worlds=["hello" ,"hangman","india","goat"]
    "for choicing any random number"
    word=random.choice(list_of_worlds)
    turns=10
    guessword=" "
    valid_words=set("abcdefghijklmnopqrstuvwxyz")


    while len(word)>0:
        main_word=""
        missed=0
        for letter in word:
            if letter in guessword:
                main_word=main_word+letter
            else:
                main_word=main_word+"_ "

        if main_word == word:
            print(main_word)
            print("you won!!!")
            break

        print("guess the words ",main_word)
        guess=input()
        if guess in valid_words:
            guessword=guessword+guess
        else:
            guess=input("enter the valid characters")
            guess=input()

        if guess not in word: 
            turns=turns-1

            if turns==9:
                print("9 turns left!!!")
                print("---------------")
            
            if turns==8:
                print("8 turns left!!!")
                print("---------------")
                print("       o       ")

            if turns==7:
                print("7 turns left!!!")
                print("---------------")
                print("       O       ")
                print("       |       ")

            if turns==6:
                print("6 turns left!!!")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("      /        ")
            
            if turns==5:
                print("5 turns left!!!")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("      / \      ")

            if turns==4:
                print("4 turns left!!!")
                print("---------------")
                print("      \O       ")
                print("       |       ")
                print("      / \      ")
            
            if turns==3:
                print("3 turns left!!!")
                print("---------------")
                print("      \O/      ")
                print("       |      ")
                print("      / \      ")

            if turns==2:
                print("2 turns left!!!")
                print("---------------")
                print("      \O/ |    ")
                print("       |       ")
                print("      / \      ")
            
            if turns==1:
                print("1 turns left!!!")
                print("---------------")
                print("      \O/_|    ")
                print("       |       ")
                print("      / \      ")
            
            if turns==0:
                print("you losse")
                print("---------------")
                print("       O_|    ")
                print("      /|\      ")
                print("      / \      ")
                print("better luck next time..")
                break 

print("you have 10 chance to guess the currect word")
hangman()
