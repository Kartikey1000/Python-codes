#only the words
WORDS={"PAIR":4,"HAIR":4,"CHAIR":5,"GRAPHIC":7}

def main():
    print("Welcome to spelling Bee!")
    for words, points in WORDS.items():
        print(f"{words} was worth {points} points")
    

main()
#the game
WORDS={"PAIR":4,"HAIR":4,"CHAIR":5,"GRAPHIC":7}

def main():
    print("Welcome to spelling Bee!")
    print("Your letters are : A I P C R H G")

    while len(WORDS)>0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")

        if guess =="GRAPHIC":
            WORDS.clear() #clear all the keys present
            print("You WON")
        if guess in WORDS.keys():
            points=WORDS.pop(guess)
            print(f"Good job! You scored {points} points")

    print("Thats the game")

main()



#better version of game 
WORDS={"PAIR":4,"HAIR":4,"CHAIR":5,"GRAPHIC":7}

def main():
    print("Welcome to spelling Bee!")
    print("Your letters are : A I P C R H G")

    points =0
    tries=3

    while tries>0 and len(WORDS)>0:
        print(f"\nYou have {tries} tries left!")
        guess = input("Guess a word: ").upper()

        if guess in WORDS:
            earned =WORDS.pop(guess)
            points+=earned

            print(f"Good job! You scored {points} points")

            if guess== "GRAPHIC":
                print("You won!")
                break
        else:
            print("wrong guess!")
        tries-=1

    print("\nThat's the game!")
    print(f"Your total score is: {points}")

    print("\nWords you didn't guess:")
    for word in WORDS:
        print(f"{word} - {WORDS[word]} points")

main()