import random

def main():
    while True:
        try:
            n=int(input("Level: "))
            if n>0:
                break
        except ValueError:
            pass

    number=random.randint(1,n)

    while True:
        try:
            guess =int(input("guess: "))

            if guess<=0:
                continue
            if guess<number:
                print("small")
            elif guess>number:
                print("Large")
            else:
                print("Right")
                break
        except ValueError:
            pass

main()


